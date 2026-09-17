# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12efe0c1-c585-35b3-a907-8288c2c759ce | -9.11176 | -65.93589 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94f6fdf9-2aae-3b49-89a1-ec8fb6d6ef80 | -11.60783 | -50.63177 | 2026-09-17 05:18:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba70139c-32e0-3565-8bde-680b00bfde46 | -12.43353 | -50.79472 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06278d98-52f2-3ca6-bc1c-a079f6ff1039 | -9.28222 | -60.62873 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 171d0b51-867b-3ed7-b081-a44d853e4f27 | -12.45476 | -50.8376 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a3da0c06-8f59-30d3-85ff-d43463b55909 | -12.31799 | -47.95789 | 2026-09-17 05:18:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29ff907e-f876-3b2b-b2c4-c429fdc64461 | -15.46969 | -53.7797 | 2026-09-17 05:18:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5448833b-8b3b-38f5-ad9e-eefd4c257a84 | -9.69856 | -58.1786 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b0a0820-d1b5-3339-a21c-3678f361ffc9 | -10.79693 | -50.84938 | 2026-09-17 05:18:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a376c32-4a4b-3957-90f5-2eed401910e1 | -12.45063 | -50.80158 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1bacc4f4-5eb6-3cbd-97d1-9cb02d220cff | -9.77469 | -60.46548 | 2026-09-17 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76d5f2e3-d9ec-3587-b601-3a21e2bc8e11 | -8.9207 | -62.40465 | 2026-09-17 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c902329e-1bbb-333f-94fa-ca09480ecf9c | -10.98026 | -48.30591 | 2026-09-17 05:18:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6daa1d71-6861-3780-83d8-feed950ebc8c | -12.10772 | -57.19898 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95a8e658-c2dd-38c8-b6e1-350e437c7abf | -11.98326 | -52.45877 | 2026-09-17 05:18:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 833f4586-adc0-308c-a984-e5f7e94cbb05 | -8.6437 | -66.58073 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40274d73-5b49-3dd8-9cec-fb170ca6e0d6 | -14.39206 | -47.27592 | 2026-09-17 05:18:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5becd822-b84f-39b1-98a7-7834f9191917 | -12.10515 | -57.19873 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac282864-4eda-3b83-a03c-701a5f13b334 | -12.10683 | -57.18814 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65c59acc-5876-377b-b649-f52ced13f3b3 | -11.13072 | -49.04426 | 2026-09-17 05:18:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d3fc27a-dfd5-3eb0-9034-be24b0a8edd2 | -8.63822 | -66.58195 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24da591c-c7c7-3745-9e7f-2bf2530e14b9 | -10.65853 | -58.76485 | 2026-09-17 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f4465e3-1737-3b2c-98ad-99182950d245 | -12.43005 | -50.82085 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 26673d84-37a0-3dd9-927d-1341fd38e303 | -10.83746 | -46.15796 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 53a0ea35-2d50-33e1-86fd-b7c4c9fd82ed | -9.62803 | -61.82329 | 2026-09-17 05:18:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47c90986-7d23-3637-b6ea-f16efd0a5056 | -9.17523 | -58.30371 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37a4e7f3-02ec-3b49-bdde-18237749ff7b | -11.53517 | -46.87402 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40c6c1ef-f9b2-35bb-80c1-0b4940eb854a | -12.44829 | -50.81899 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f9a5b3c-5324-3aad-9284-cc24593fc59f | -10.39101 | -58.3034 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da134036-e34e-3ae4-95e4-de8464b03a32 | -12.31755 | -47.96136 | 2026-09-17 05:18:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cc255ec-7d62-3c75-86c2-3f01466e6679 | -8.75325 | -66.57448 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7c25b0ec-cba6-35d4-8ed0-731363b2d802 | -11.81207 | -58.18123 | 2026-09-17 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 00cc4afb-a5ca-39e7-8571-853a53679665 | -13.60233 | -46.94919 | 2026-09-17 05:18:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27a3c2f8-954c-3192-84a6-fcea1886b65a | -12.43331 | -50.83015 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8477b5ce-2d56-3e0e-b3f4-0503fa56e289 | -8.638 | -66.57964 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5778b53b-2728-3b75-abfe-e2da2f338432 | -12.37567 | -48.46545 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3575974a-230a-3428-9bfc-2f22b01c6e23 | -10.98795 | -59.13695 | 2026-09-17 05:18:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| baee0493-a1e4-33b6-b3ad-740af080fca5 | -7.6016 | -67.32197 | 2026-09-17 05:18:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82bd1ed9-0cc7-3ef1-a5a0-debf2653f648 | -14.56106 | -46.60788 | 2026-09-17 05:18:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e895647-a9ac-3716-8ccb-0fe291ee67c9 | -12.44296 | -50.79161 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 38187aad-c408-313c-9104-1f9704988c5d | -12.14647 | -48.26299 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bb6d42e-25f2-3ba9-a3ec-765811c0ff9b | -11.89111 | -47.58052 | 2026-09-17 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47fbc41f-c375-3f53-b629-17e413c7f72b | -10.387 | -58.30655 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c42d2213-7433-3e4e-8651-119d5dac3b03 | -12.45325 | -50.74842 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fd07aca-5b92-3bd8-8d12-933448c69354 | -12.10627 | -57.19167 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dad383e-513a-3dff-bac8-c20a619086e6 | -12.45356 | -50.77974 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b9720981-e623-3c82-bebb-65cfdd5f82b6 | -11.3184 | -47.06641 | 2026-09-17 05:18:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3abd21de-822d-32b8-b1e2-14c5662a4c9b | -11.53247 | -46.8611 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a31f26e-09cb-35b1-8e24-ffd8a13057e7 | -12.85384 | -44.38859 | 2026-09-17 05:18:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ca6e880-6e76-3045-8f37-f492e283cdb3 | -8.92141 | -62.40053 | 2026-09-17 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f8d8552-943f-3bbb-b8e7-bc8b08990da2 | -11.56417 | -46.88548 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58567507-f6b6-39a7-864d-9a2c64065f18 | -10.39441 | -58.30397 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9ebde67-2675-3642-9523-704fd0104eb7 | -11.57609 | -46.88258 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57d43283-1fc7-3d52-9428-a8497cdb0aeb | -12.46771 | -50.80842 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb0ea272-c311-32d7-920f-9ac2183ae472 | -12.20341 | -52.86923 | 2026-09-17 05:18:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b122910-1334-38cb-ac9d-71d7f8ced2ef | -12.95301 | -48.6143 | 2026-09-17 05:18:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8019ffb-d41c-3423-85c9-2b8c702348fa | -14.84166 | -59.54733 | 2026-09-17 05:18:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a42bb4bc-f752-3fd7-8ab0-be0ab1134b36 | -9.90999 | -57.0652 | 2026-09-17 05:18:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0e21cf3-5f16-39c3-a207-eb48f645646d | -12.40119 | -48.4783 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3794c226-c58c-3f9a-a329-8d89607c1beb | -12.5165 | -56.90296 | 2026-09-17 05:18:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5383631c-6359-304c-a6ec-db6d281bf0aa | -11.56989 | -46.88594 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dab930c-bb85-375e-8bb5-abe76d383060 | -11.48614 | -45.73774 | 2026-09-17 05:18:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa5dd589-a13f-3860-965e-f2a5061b2987 | -10.76538 | -46.20845 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13a8b68c-6220-3dd6-8b31-18624bb15fee | -13.60762 | -46.95432 | 2026-09-17 05:18:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdc65c56-b4d5-3dfa-9746-4745b27e521a | -10.39781 | -58.30454 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb2907b0-1a00-3102-99c9-36aa553887c7 | -9.10191 | -60.978 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51367e78-795e-3b1f-b3e2-c9d990c877d6 | -13.75329 | -48.80898 | 2026-09-17 05:18:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61fd71d8-4df3-32ad-bd2a-970a5a32a022 | -8.63896 | -66.57802 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc168fdd-b029-300a-9f18-b7b7b98d95c2 | -12.45094 | -50.83264 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe6f6243-0866-396d-a809-555c519417c0 | -12.44744 | -50.85863 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b8ede27-fccb-30b5-98c4-8e59da1e2e9a | -12.44796 | -50.78787 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d9532013-8d6a-3dce-a6bc-ac7dc95d118e | -12.41086 | -50.79595 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b44e240-286f-3b08-992a-8408837af5cf | -12.45184 | -50.85925 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff521a6f-21b4-3e6d-9944-550c4c475877 | -12.42622 | -50.81588 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6c1b6033-d800-3c26-9adc-ed9172c5c6c9 | -9.096 | -60.96358 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41e5d545-0287-363e-96c1-a7cb95f1af78 | -8.75399 | -66.57053 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| daad99dd-5975-368f-8c2b-e03559e2fb30 | -8.9164 | -62.40385 | 2026-09-17 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f311438b-66d4-30db-bd8b-c8e777d806c0 | -11.54189 | -46.87876 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 680ef124-ead2-3015-89be-ce76b3bad986 | -12.10828 | -57.19544 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f5c856f-2627-3ad2-bf34-af33d7ea1806 | -10.83106 | -46.16119 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c52253fd-c270-3f54-ba16-9a31f7330879 | -13.38407 | -57.0211 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24f72496-905f-3547-a8dc-62dd25caba00 | -9.69455 | -58.18172 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c9213b4-9f40-3d07-91fe-6c99c5ecf6a2 | -12.10884 | -57.19191 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bae2e97-d50a-368f-a6de-20bb55deb3ad | -9.46104 | -56.7013 | 2026-09-17 05:18:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47d82480-5d54-3e32-9e20-92662882c362 | -11.60842 | -50.62743 | 2026-09-17 05:18:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96b95d1e-7234-32b1-a1b7-beb9ecf05286 | -11.88478 | -47.58688 | 2026-09-17 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c977d643-dbbe-3337-8b03-8cd668cd3873 | -12.13771 | -57.18216 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4337043-bd3f-333a-926c-c530d7f44e72 | -11.89023 | -47.58756 | 2026-09-17 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92fc1b53-4bd6-39ca-8070-70af027f5adf | -12.45121 | -50.79722 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d852b323-4d0e-3e95-b77f-861d22a75fcb | -13.75361 | -48.80629 | 2026-09-17 05:18:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dbfdbd7-7301-3284-afe8-a9e21ab2e5a2 | -14.13814 | -44.01501 | 2026-09-17 05:18:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4fa6df5f-e701-3c35-b1a0-ad84f6aefe5d | -10.83538 | -46.17452 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ab996af-9e4b-3d7c-a963-b7bd6dae8747 | -12.4383 | -50.82643 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| d5df3fdd-32ab-3086-bdfa-d2f3c61bfb63 | -11.33032 | -46.77276 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbdb0282-c7f1-3aab-bfb1-2a5384274fcf | -11.89623 | -43.82624 | 2026-09-17 05:18:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6bd87dd1-31cd-3d48-a49c-1a02b41bd9c7 | -11.48225 | -45.77026 | 2026-09-17 05:18:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42993ae0-a07d-30b8-a835-72a12bb8d9a0 | -10.3898 | -58.3108 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 812f6089-5d7f-37d4-973b-94578d82bd7f | -12.11329 | -57.1854 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f286b8b-ab96-3bbe-8c36-35ef23afc7ee | -12.4297 | -50.78973 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7cd67d45-642c-39ab-b097-c19bec4cb403 | -8.91783 | -62.39563 | 2026-09-17 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README68.md)
