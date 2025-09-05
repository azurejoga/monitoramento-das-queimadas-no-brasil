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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35685b76-c5fc-3301-82f7-deab2bf1d314 | -11.92582 | -46.65179 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c647e57-9038-3db9-8a4d-dd42a012346f | -9.81881 | -46.65293 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c7309b6-f3f3-3415-9d14-92cf7d32623d | -10.88396 | -55.38966 | 2025-09-05 04:36:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4da4739-e7c3-32b3-b973-62e504086b9d | -12.09303 | -44.72046 | 2025-09-05 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0a42d3f-5f9d-3dac-a98e-7b49892ab674 | -12.43973 | -44.74699 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27df2d2d-7b20-3355-9d44-d43dbd8bef28 | -11.20048 | -55.02546 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edf90b9a-0ceb-33e3-879b-9addd91493df | -10.98658 | -45.92884 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c699ef3-2974-3d1b-b38e-63328679bb92 | -11.92231 | -46.65133 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e53b48c-21c7-383c-8ba6-eed649107c02 | -12.48574 | -53.84584 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 106280d6-a7d5-306d-87b1-0e6d5ef10b6f | -8.87293 | -52.02639 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d026ca26-859c-3e22-85cc-6d361802fa06 | -8.09353 | -45.34347 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c5a0cd6-cc48-306e-a4ab-e33a55c73bf2 | -6.32565 | -58.17147 | 2025-09-05 04:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 955473f6-c34d-3e2c-976e-f14d5ea9cc16 | -11.00335 | -45.91462 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6ee6e08-08fc-3292-a71c-e6f9338494b0 | -13.27869 | -46.81912 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64df94c6-e9c6-3d56-8a88-6009b1e73ca4 | -12.71089 | -45.0849 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcf643f2-65d9-37e5-901b-b19c881c4b9d | -12.1855 | -53.89046 | 2025-09-05 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e733d19-313e-3386-be73-d39ebbe1d26d | -8.09588 | -45.35202 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5da840a0-83c4-38f3-a9e4-2bcdce4f339f | -8.47974 | -45.08048 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f05f3d0e-1b62-3a1e-abfb-7f2eca612240 | -11.5993 | -47.75016 | 2025-09-05 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7acad91b-c1d6-36b2-8be3-27412e140e9e | -9.69884 | -48.97823 | 2025-09-05 04:36:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 840aab19-5ace-3e72-a2cd-42ce1a4c8818 | -13.00667 | -45.21741 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 63db1896-23d4-312b-8037-3c0e2c15490a | -10.08767 | -48.05835 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0041129d-9261-3a3f-a4f5-36238fed98e0 | -7.75859 | -48.78426 | 2025-09-05 04:36:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e2cf1f5-dc64-3b09-88d1-4b8934c0d021 | -5.48886 | -60.12659 | 2025-09-05 04:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa955355-c17e-303c-ba27-82fe339d7dbb | -10.97917 | -46.00315 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fde6782-50f6-33b8-ba05-c335d7e184d8 | -10.52569 | -57.7762 | 2025-09-05 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ad01da7-c294-38b0-a64b-f71c2901701b | -10.47432 | -53.62692 | 2025-09-05 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25ee94f3-4e7d-300e-a3b9-16299f3a72a7 | -9.42341 | -46.7765 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fbe6703-2375-391b-99fc-56d76df34509 | -13.0024 | -48.06451 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e62d7a71-901e-315e-a352-697b68efb484 | -12.24296 | -50.14033 | 2025-09-05 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f409de1e-f583-3af1-b8ea-4822157d63c9 | -13.71532 | -46.90707 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d1dc333-da89-35f0-b39c-b5fde27443cc | -8.08672 | -47.57706 | 2025-09-05 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e22aa08-db26-3a1c-893a-5184a63dfbd2 | -11.38384 | -43.54784 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e09a13f-a304-39dc-b752-48909527d383 | -12.97934 | -48.05709 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74ca30ef-61eb-30bd-8ef3-41383d51a01e | -8.90647 | -45.86279 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96cd2a61-9b19-3a62-9da6-6bd168523ee5 | -12.99339 | -48.05558 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07f23f7c-8f20-3364-b24d-5f348d56c564 | -8.52126 | -51.3218 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3837bd4-0b20-3e75-99b5-70006cab8bfb | -10.97673 | -46.01947 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc24e8e8-04ff-33cb-894b-8a4d58611b03 | -12.9732 | -48.07476 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b416b98-694b-387f-9050-415b7446ac54 | -10.96262 | -45.96714 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca0fd54f-984c-32b8-95f3-8ef06ce58cfb | -12.9799 | -48.05338 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0b98ae9-201b-37d9-b401-b745fb39e32a | -12.00035 | -46.75893 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70b2a686-f817-3d14-af2a-37c9901484a5 | -12.51978 | -53.83639 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 482d62cf-92d6-35b7-a2de-37d02badbcff | -8.08104 | -45.32957 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8a29b3e-fa33-3562-bf45-1686e3ed9930 | -9.48526 | -54.42414 | 2025-09-05 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bd4a0f2-5713-3ea6-960d-f7f4927c2c07 | -13.55813 | -48.1244 | 2025-09-05 04:36:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cc8229e-404c-3062-b98c-3df1dc950096 | -11.39417 | -43.59533 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60a3410a-9c31-3d7a-ada8-9b9bd7eb5d16 | -11.84847 | -47.5373 | 2025-09-05 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ab3e96a-d0b9-314f-88d2-f80a08cddb3a | -9.76694 | -49.4201 | 2025-09-05 04:36:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b15d45d8-71b5-345c-912b-aaff66cf215c | -11.62001 | -52.20268 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d8acdf97-96f6-3793-90de-dceb299602fb | -10.75936 | -47.73366 | 2025-09-05 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59edf2ec-2129-3861-9f77-0a29379a4aa1 | -9.49922 | -57.82265 | 2025-09-05 04:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28009a7e-ec52-3a6d-838d-b6b247d54ced | -13.66175 | -46.95226 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48224250-ba88-3b1e-b113-3b9e110f3eb8 | -7.69946 | -50.30222 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10f9df44-3da6-3ee2-9f56-13b87533aff9 | -12.4716 | -48.09322 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2a8bfa8-bbfa-3eb3-bf18-69bc57372477 | -10.52971 | -57.78387 | 2025-09-05 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7308d5df-b885-345a-9808-f3d0e3c4415d | -9.86915 | -46.571 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 519e8372-5b44-31fd-be98-053a526eaed7 | -11.96824 | -46.77427 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da92f56b-7028-3819-a676-2a9fd0feed6e | -11.8301 | -51.44036 | 2025-09-05 04:36:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cf08ee3-8c4b-3506-bb27-504b2ad372be | -13.28285 | -46.81525 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80671fdc-6586-345a-9cf6-cd12dca8bc43 | -8.97161 | -44.45704 | 2025-09-05 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5698b4d5-8f3a-3455-89d4-e7c31221374d | -10.99517 | -46.01806 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d586ab4a-bdfd-3f8d-b5bf-dde02234eed0 | -12.51979 | -48.07129 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62be4f4d-ee33-3dec-a470-89cc5ce7c2d0 | -11.63821 | -52.22776 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9f65a311-a0b8-38f3-b382-4b95e82ce1a0 | -7.68968 | -50.29658 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a954535-8ebe-3719-80cf-f5f550904493 | -13.74832 | -46.92756 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f13b0c8f-6f13-3dd0-9246-571a7d21f851 | -11.10356 | -52.0284 | 2025-09-05 04:36:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8448264d-3327-3ff7-a018-bfffff5f1a82 | -8.81768 | -47.51126 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d7c42ce-a380-3b9d-9674-2b6b70df6abe | -12.95098 | -48.05686 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaa07c05-c3cd-3298-9ca8-b7aff0ddb88d | -12.32307 | -47.05127 | 2025-09-05 04:36:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5de201ae-d495-356d-aeff-fd11b4d4ebde | -8.89828 | -45.77269 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ccf3450-7b8a-36d5-b5d7-838fa08fa337 | -12.72304 | -45.08186 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d65c470d-2c8d-367e-8fce-fe5449756ce3 | -8.01641 | -44.7743 | 2025-09-05 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca548ea1-aeb2-355d-ade5-a89573855d72 | -11.0057 | -45.92339 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4b8703e-b39d-33e1-b111-7d2286c6766e | -9.81823 | -46.65669 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2f20c2d5-d6c7-3738-8c9a-d135dfd03198 | -10.1011 | -46.24422 | 2025-09-05 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb96b8d9-df31-36bf-b438-8ea3f197f444 | -8.08284 | -47.58006 | 2025-09-05 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ace3681b-9790-3c05-a7be-92cdde8148e9 | -12.86978 | -48.01498 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6be4a6eb-ac7a-3ef2-b1c9-8abf6a0cca5f | -8.07989 | -50.19958 | 2025-09-05 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebd8b61e-1bab-3436-96a1-d93bf532771f | -11.72486 | -47.75089 | 2025-09-05 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fb56783-d371-3bb4-beb4-ce5a670db3fa | -12.97179 | -48.0788 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af9c5ea1-7e53-3395-a19f-fe9da1331960 | -11.92172 | -46.65527 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9c64a3d-c7e8-3377-b21a-1ebaa46b1e26 | -8.52055 | -51.32611 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 366bd691-0f54-3296-8027-3bdd677cc6e5 | -6.32416 | -58.17971 | 2025-09-05 04:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a232576d-76c8-3c1e-a06b-befde6eac563 | -12.4122 | -47.49771 | 2025-09-05 04:36:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1323475a-4680-3300-9d1d-74d4f15284b6 | -9.44676 | -46.8067 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b582def0-9790-39e6-bfd4-cd286ccdd0ec | -10.72297 | -47.94794 | 2025-09-05 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f197fab-a51a-379d-8a83-e0666ac4330a | -10.97151 | -45.98104 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9219e55e-9d32-3ca8-bbb0-c565764bc6a1 | -13.34859 | -46.83351 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b75f43e-4156-3858-aa9e-97a0350c0835 | -10.44817 | -53.61172 | 2025-09-05 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f6944c8-e896-3d06-8ca7-33a7978612ca | -10.76689 | -48.2816 | 2025-09-05 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43dd0048-0dca-3be3-94d5-c219c49c7c6f | -11.58424 | -47.89219 | 2025-09-05 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f9c48a3-2bb1-31de-a33b-ab82c2df56b8 | -11.59892 | -52.15095 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dad789b3-6980-3906-a94b-246ee11709cd | -8.7544 | -46.10717 | 2025-09-05 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da2ea467-fa50-380b-a70f-f01ad8093f20 | -9.79771 | -48.31464 | 2025-09-05 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 785132d1-55f7-39bd-b22f-eb031966a624 | -8.35394 | -52.55032 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d393e3e3-2843-302a-a0fc-1dc9636920e9 | -10.96323 | -45.96301 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaaaa4bc-3d6b-35ca-95cc-015452e9e84c | -12.49066 | -48.08137 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97514cc5-e634-3195-96b7-09995e342f77 | -11.26833 | -48.33588 | 2025-09-05 04:36:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 443a3a07-257e-396f-a3f1-ca0ad510a723 | -11.74549 | -47.75715 | 2025-09-05 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README30.md)
