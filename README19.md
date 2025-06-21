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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 981b7e5c-9087-3a43-9df6-cc7429c08068 | -11.27991 | -46.65091 | 2025-06-21 04:59:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf4cd01a-a2a0-3242-9f31-979e463bd965 | -10.52255 | -53.62831 | 2025-06-21 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35b34773-af2d-33e8-a279-4407021a8245 | -10.8615 | -53.76248 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14b2d6e7-a634-3390-9380-7967a1fed3be | -7.27706 | -45.36489 | 2025-06-21 04:59:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d213f4da-8f5d-312b-bfcd-eae9ae959bf2 | -9.60248 | -56.28449 | 2025-06-21 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e4ffd0a-b8c2-3900-8779-a5b5a3c16659 | -10.86205 | -53.75882 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b789343-4663-3242-b610-058a751540c7 | -11.29368 | -46.66658 | 2025-06-21 04:59:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e4e1895-b471-33fd-93b7-d134fa539919 | -9.48517 | -56.07671 | 2025-06-21 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 535277ec-f0b5-3b20-8cee-24db339afd3e | -10.87168 | -53.76405 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b82f402-b17d-3515-9761-363c2fb6871e | -9.25607 | -57.53176 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 736f4b72-9433-3d2e-87e8-a32028844b70 | -10.52028 | -53.62043 | 2025-06-21 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eff02c32-fc56-3a2c-9621-a755b16404e4 | -7.21946 | -43.073 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 23b8cd9c-0978-3751-9443-d46991415492 | -10.30231 | -57.13765 | 2025-06-21 04:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24f5593f-2c9e-3a1b-87e5-114d9c2b4d5f | -7.94187 | -48.03839 | 2025-06-21 04:59:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 786ef560-bab3-3e43-ab05-8b16812fc2d0 | -11.21161 | -47.83815 | 2025-06-21 04:59:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1026062f-1ef8-3661-99b2-02497da565f7 | -9.46824 | -57.8387 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5116fe31-1519-3f17-8df0-1746853dcd09 | -9.35098 | -57.01574 | 2025-06-21 04:59:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88c21c35-3453-3a1b-a1a6-637875d852d2 | -10.86545 | -53.75933 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16045b4b-dc92-3ddd-933a-37781d407ae8 | -7.22463 | -43.06556 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 08110d2b-5dfa-3eae-b632-cbadee86f84a | -8.00715 | -47.66867 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39284a16-c313-3a7c-a3fe-7602131f3837 | -8.03214 | -47.65802 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26d0e0b5-829b-39fb-b473-c0a5bf0168d8 | -9.26872 | -57.82385 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b4f6d41-3d42-37af-96a3-f81efda242bf | -10.86094 | -53.76614 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc1b5b36-c6d3-3a91-b652-da48c6df4ba6 | -8.12419 | -61.41505 | 2025-06-21 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9eb4bd33-56fe-33d3-b192-54b4612da144 | -8.7359 | -47.98438 | 2025-06-21 04:59:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0309130c-e7b4-353f-a9f5-f98dd22bb409 | -9.41916 | -48.43468 | 2025-06-21 04:59:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ded7d16b-8ff3-35ef-a558-119b7697e248 | -8.98229 | -49.86433 | 2025-06-21 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06f6bd8b-7d40-31b1-8c5a-7b5ed5c09229 | -9.09484 | -50.02743 | 2025-06-21 04:59:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 94b1e51e-d669-3361-ade3-83d3d085c42b | -9.41593 | -48.42516 | 2025-06-21 04:59:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8798fd5-7dd9-3ad5-86ba-0db831994de9 | -8.98631 | -49.86492 | 2025-06-21 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0d8c209-8158-3300-9e7d-fff822e55789 | -9.48795 | -56.08085 | 2025-06-21 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8689cda-7e98-3cdf-91db-498f5c7c90a1 | -10.95353 | -49.25247 | 2025-06-21 04:59:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a58ce75-dffb-3fd0-a999-a4282ec92141 | -7.22564 | -43.07394 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f21dc525-4378-3d48-a3a4-28694fc06225 | -10.86635 | -54.31529 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2793268-fde4-399d-b389-34f1d78bb2a9 | -11.1402 | -53.92188 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67ce1c7f-8e6d-33ad-a065-4715df36518f | -8.70427 | -50.04935 | 2025-06-21 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5d910c6-85fe-37c5-bdd7-1a87faa2bbab | -10.52708 | -53.62149 | 2025-06-21 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 592ac632-69e2-34c3-887a-8eb77918f84f | -11.27348 | -52.4662 | 2025-06-21 04:59:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e3fadfb-1048-378a-81ea-d98854212038 | -6.53056 | -55.02173 | 2025-06-21 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e20c9c6b-8d60-3b3e-9e0d-6b25d8667e74 | -8.02688 | -47.66202 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a35857e-2e20-3755-adbb-21b2cd48facb | -10.46375 | -47.03546 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b4a4d7ec-eb84-3e66-81bb-f27a64498bf8 | -10.52312 | -53.62464 | 2025-06-21 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a173f50e-ce75-333d-923b-decc32a4f1cc | -7.27799 | -49.99111 | 2025-06-21 04:59:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9849feee-45c4-3de2-9047-d188b5c5949c | -9.46893 | -57.83462 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 47da3c75-0ef5-3c3c-9e7e-28f70943de51 | -9.01291 | -61.22333 | 2025-06-21 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cea5d7c-c8cf-3864-aa9a-dacf2f3cfc3c | -9.46536 | -57.83401 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da78eb03-ee4c-3023-9c53-2fc7d5005aae | -10.5226 | -47.5796 | 2025-06-21 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6cf417e5-3a3d-35fc-a1ad-8f5e8392a3ec | -7.22339 | -43.07514 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 42a42fa5-9ee4-3e40-9c6e-731a984ad053 | -7.2263 | -43.06919 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 85e78856-10fd-3697-996e-cc3cceebf115 | -9.12245 | -49.6612 | 2025-06-21 04:59:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0caa0396-9c37-3051-a3bc-284be2f22588 | -11.13794 | -53.91402 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4d0b638-3ee1-3fe8-8af6-0983b9c4074d | -8.01832 | -47.65593 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92841c56-9a48-341c-9371-b7fc3d763446 | -9.41854 | -48.43914 | 2025-06-21 04:59:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 981a0707-1171-3f5e-ba4c-4f62569dc548 | -10.81551 | -54.04226 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2e1310d5-2c3a-3129-bcb4-4a39acdc96b6 | -7.23183 | -43.07486 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e4f02a02-1746-31b4-8d58-d2553f8b787c | -9.73637 | -48.32868 | 2025-06-21 04:59:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64e823cc-e66e-38dd-a733-c1697a40390e | -10.45954 | -47.02887 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5aca5143-9760-3d05-b6ff-bdb3858b0f1c | -10.44807 | -47.03893 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e4fb7e0-9598-3f75-91c6-18a293cd6489 | -10.03002 | -54.31925 | 2025-06-21 04:59:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9a038b33-a4e8-305a-a74d-eff7a95a0831 | -9.46041 | -57.8416 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c959b2c5-1b7e-3025-bfe0-fdf9f4bbb769 | -9.48737 | -56.08444 | 2025-06-21 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de78c01f-9531-3765-9cda-d3f71a6cdb12 | -9.47607 | -57.83588 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2954be3e-11f5-35aa-9240-53a27e0dae11 | -8.17171 | -47.79086 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76a123ef-64cb-360f-84e5-07ee385073b1 | -9.47332 | -57.85228 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9453ef48-f81e-3a46-8cd9-489ab13e99bc | -9.26091 | -57.52435 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e47c485a-a9e6-3acc-8ae0-94dbdeb39cef | -10.45456 | -47.02809 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6b2be067-2ee6-3837-8927-8f980a5bea7c | -9.4818 | -56.07616 | 2025-06-21 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffdab09f-3a5a-306d-bccd-7f47b4d84388 | -9.47044 | -57.84754 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ba3f77e-bddd-3b5c-b4a6-2214ff81f78d | -11.28933 | -46.65954 | 2025-06-21 04:59:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| facea5d4-ba54-34ae-8b02-9aede5cebed5 | -9.25672 | -57.52778 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ddadf6a6-0cee-3ba1-8798-54a464ae7d43 | -9.91805 | -52.44436 | 2025-06-21 04:59:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 464d4d52-180e-3400-9000-6a823b9b0ffa | -9.0313 | -61.22215 | 2025-06-21 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c503acb-e01b-3d18-907a-57413bee0610 | -9.02539 | -61.22991 | 2025-06-21 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed5ac202-63cc-385a-9643-673852f02631 | -8.02753 | -47.65734 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fd2dfc9-f875-339b-9708-991a746fabe1 | -9.33611 | -47.82824 | 2025-06-21 04:59:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ae33bd4-5d9e-336e-92fe-cc7d9d11620f | -9.47812 | -57.82359 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7139b3ff-8f4d-38e9-b73c-4a9f56636f08 | -8.91334 | -49.85106 | 2025-06-21 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 044353f6-ba76-38e1-9aa1-23cf35fadfd1 | -9.91453 | -52.44383 | 2025-06-21 04:59:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dbfade2-fa08-3032-8f56-cbd0ea4ee2f9 | -7.95482 | -49.27631 | 2025-06-21 04:59:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e467fff8-9259-34f6-b774-191ecd9194a3 | -8.02162 | -47.666 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e99b64ad-418a-3f76-902d-21e0eeab775a | -9.26078 | -46.90677 | 2025-06-21 04:59:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd65f17e-b02c-3979-9c79-97300aada213 | -9.35159 | -57.01199 | 2025-06-21 04:59:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16eedf3b-fc9b-381e-aa4e-0f2bc2b76908 | -9.02022 | -61.23349 | 2025-06-21 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0663d78e-6417-347c-a4c5-f1080d00ad55 | -11.07617 | -55.05246 | 2025-06-21 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4d55a80-fea6-3330-a61c-764371459822 | -9.47401 | -57.84816 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85207488-5a7c-33ad-95a5-b111b49968e2 | -10.15004 | -48.98939 | 2025-06-21 04:59:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e52e8f11-52bb-3081-8950-574eda8894c3 | -10.67699 | -56.55196 | 2025-06-21 04:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fd051f4-7807-3974-b85f-aa9334af3e10 | -11.10148 | -46.68367 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d2fe502-41fb-317e-a50c-0cd56ab129d9 | -11.10661 | -46.68458 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a42e547-fd7d-3767-a5f4-914cbad9e646 | -10.68036 | -56.55251 | 2025-06-21 04:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cfa23de-f96f-3f84-8ff1-9475020caf6d | -8.37637 | -46.97286 | 2025-06-21 04:59:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 662db707-47eb-346b-9db8-a290eeb05d5f | -9.01504 | -61.23705 | 2025-06-21 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60f3c9f7-faf6-3971-89ed-51782efed061 | -10.29826 | -57.14084 | 2025-06-21 04:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0a8559d-2a48-30cd-8ff4-82f605f15d21 | -7.80628 | -46.05419 | 2025-06-21 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87655161-1b36-3f12-a757-5683e1df8475 | -9.26026 | -57.52834 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b22b28fb-bb90-3cb8-b6f2-b219dc28d83a | -11.13738 | -53.91768 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd0d4651-c8cc-3435-b465-ec81b36b9a30 | -9.46756 | -57.84282 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d8a033f-bde3-3431-bb89-9ef436f60212 | -10.44733 | -47.04462 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 38e1490e-cf10-38f4-914f-ebe0006d880b | -7.26682 | -45.36019 | 2025-06-21 04:59:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba5cea31-1be1-3aa4-8b70-c8bff6a9431f | -10.02613 | -54.32226 | 2025-06-21 04:59:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README20.md)
