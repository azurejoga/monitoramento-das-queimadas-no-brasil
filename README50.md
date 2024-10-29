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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76b3d3ea-4cea-3c91-87a3-c0b7004441f8 | -2.87148 | -51.31352 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2371cfc-fd6c-3fc3-a5b0-f2f939d89f8e | -2.82904 | -51.03558 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8a9139a-4ee3-3d90-b805-ce15acc0c75c | -2.82555 | -51.03508 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d4ac304-22a1-3eac-8f7e-eecd7aa7b03f | -2.82493 | -51.03895 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07ab1edd-6c8a-3d2b-a657-2b1590d2faf5 | -2.79328 | -51.46138 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f88c652-c312-3789-ac83-0845f896af08 | -2.79028 | -51.3666 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96f93b4e-28f9-3ed4-93a0-e0f8de5fdc2c | -2.78973 | -51.46082 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 378ef68c-9c24-36b7-83d7-8146cf5f986d | -2.8837 | -51.8314 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5458751-8926-384e-b276-b70c6e8e652a | -2.88075 | -51.82661 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74c02838-b46b-3e50-ab8f-0d2efa064913 | -2.84367 | -51.8036 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 41805511-381c-3d7d-9b5f-ba366aaf5aee | -2.84301 | -51.80777 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d26c889c-a134-3109-8e4b-4a91d4684f21 | -2.84234 | -51.81194 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ee00dff-ebf3-33c7-a4ad-4b88df55446b | -2.84006 | -51.80304 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a84e972-8c4c-3ecb-a7c2-fb4579ca5b06 | -2.83939 | -51.80721 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28ee204d-f783-3a38-a7cf-a481f6f7483a | -2.83873 | -51.81137 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28444a42-4e64-3412-8786-2b78f0c9fdc6 | -2.83578 | -51.80664 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2f532d6-fcd2-3852-9a8c-864e573617ba | -2.83511 | -51.81081 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd88ee88-3731-34c1-a6be-c7d0774ac1e7 | -2.80325 | -51.80165 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48fffc16-9aab-354c-8385-76358ee44fc3 | -2.80258 | -51.80579 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6a0a0513-3bdc-39ff-a5bb-94639599ba6b | -2.79896 | -51.80525 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5db3fc80-7bb5-35cd-ac4f-d70d0ff688c6 | -2.7975 | -51.80612 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7200449f-2257-30fa-adee-efb5ce8ab362 | -2.79534 | -51.80471 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cda243c0-8997-3fd7-92c2-612beaa96eea | -2.79467 | -51.80883 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d1cc3b3-cdd7-3b62-86a6-5e16fd756e94 | -2.79388 | -51.80558 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf05d4c1-a092-3887-827f-908fd05ee471 | -2.79323 | -51.8097 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e91612bc-4673-3f00-9023-9117c912f0d5 | -2.79318 | -51.95555 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f7a7c0b-541f-30bb-9097-2c6a10d7a957 | -2.7925 | -51.95979 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 12a45088-b92f-370b-b5a9-c154e2b8008d | -2.7859 | -51.9544 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e755a03-3352-3057-a47a-ca725fd473dc | -2.58579 | -51.93813 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9573799c-3b0f-3df9-9436-558d416c1d2b | -2.58491 | -51.92043 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28e1ec50-cdbf-3415-b8c4-a72016622bd7 | -2.58057 | -51.92415 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ec5e257-2241-37bd-96ab-748788874290 | -2.57835 | -51.84569 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10fca53e-7463-30b6-af6e-0ba6e041ff5c | -2.57767 | -51.84988 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7abe3f93-f19d-3609-9af7-883d83a89311 | -2.57404 | -51.84932 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05b02ea7-3df8-33ae-aecb-6bceae164fe2 | -3.52866 | -51.64972 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddc5c643-7178-3de0-afe7-ca30a4fc52b2 | -3.45347 | -52.02604 | 2024-10-29 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31352f29-adbc-3512-bc9d-5991b8e46b46 | -3.63564 | -52.06145 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 347e78f3-e143-32d0-b25d-92791ca179c6 | -3.56863 | -51.98706 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ba6b152-f15c-33aa-b83a-8b4d0eab97cb | -3.62269 | -51.78821 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80bad022-9a1a-33ab-a3e1-c4aa83a06012 | -3.6008 | -52.01773 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34f030d4-f76c-3ee7-8b8f-6ae927e0a31b | -3.5693 | -51.9829 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ca9c178-66f4-3e37-b4f7-ad412cbda895 | -3.56392 | -52.01627 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6edf5a67-dce9-3e00-888f-7e1af023d7e9 | -3.80039 | -50.96213 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db47cb67-c9cf-3b3d-86d9-c546884c53c5 | -3.79979 | -50.96222 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ed22b4a-a5cd-3130-9715-ec7f807cf191 | -3.79919 | -50.96595 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82dfa259-2aea-393a-87f3-627fcb0f6491 | -3.79635 | -50.96534 | 2024-10-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1759587c-ff81-3d7d-ad4d-d5056b06e2fc | -3.67314 | -51.38243 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20f593c5-b609-38ab-a302-6fcaacf5e98c | -3.67026 | -51.37794 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e8e40e8-15f5-3d12-a676-c86406f7a24c | -3.66963 | -51.38186 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9bd27d00-ecee-3ff2-a2a6-97bf00be2809 | -3.6247 | -51.5489 | 2024-10-29 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7e5bff5-fc9f-33d9-967e-52eb8a1a9427 | 3.58194 | -51.2906 | 2024-10-29 04:38:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed0fc0fc-7bfe-393f-9fee-c6df05247d2c | 3.58123 | -51.28592 | 2024-10-29 04:38:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5da6742-5411-3f50-b226-1050809f68f0 | 3.57531 | -51.2725 | 2024-10-29 04:38:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1ea9ddc-ae56-303f-a168-32fb1d2e176a | 3.57221 | -51.27773 | 2024-10-29 04:38:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cd6a898e-d133-3153-8b0d-5e09ddadeae2 | 3.5715 | -51.27307 | 2024-10-29 04:38:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a7a62c2-34cc-3893-bd04-70520c95bc06 | 3.56911 | -51.28296 | 2024-10-29 04:38:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b37eeea1-83fc-32b3-a3f2-d9b0819480e8 | 3.5684 | -51.2783 | 2024-10-29 04:38:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b76423ce-20e1-3291-abfd-2430f5ca7b26 | 3.45329 | -51.26073 | 2024-10-29 04:38:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c939a3de-2f23-3daa-a2bf-a641a6a6a558 | 3.45019 | -51.26594 | 2024-10-29 04:38:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c38839d6-ceee-32c2-affc-bdb05712a229 | 3.44949 | -51.2613 | 2024-10-29 04:38:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c11270d-009c-321d-b934-4609d5d55b6c | 2.72524 | -51.34231 | 2024-10-29 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a04bd689-df75-3f1b-8d70-9892902007e9 | 2.61844 | -50.91636 | 2024-10-29 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45fd26c3-c5ec-3e14-b802-73e97c9f9755 | 1.01071 | -52.21913 | 2024-10-29 04:38:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 168748e4-60ca-3ec3-81b8-a4346ced642f | 0.86948 | -52.49972 | 2024-10-29 04:38:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96b720dc-d5c3-3612-af7e-fc6526ce2116 | -0.31186 | -51.71669 | 2024-10-29 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fe8be87-c4c3-35db-b2af-f027fe3c95f9 | -0.22609 | -51.54393 | 2024-10-29 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad8ebcff-371d-3cc1-8778-46f544185868 | -0.22577 | -51.54249 | 2024-10-29 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf25dda6-f28c-30a3-afe3-5e1c866af91e | -0.13298 | -51.56071 | 2024-10-29 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 604e654d-6492-3022-bb6a-686f8e0c328e | -0.1286 | -51.5645 | 2024-10-29 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d337bcf-8a22-3e54-9e8d-37777bd3d7d6 | -2.21743 | -51.9912 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d14c134c-aea0-3600-b473-3e2775c0248e | -2.21729 | -51.98962 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3b0b551-ce1c-338b-a877-5825284d078d | -2.06288 | -52.13922 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3fae67d0-95c6-3698-a504-21f8660ee002 | -2.06218 | -52.14364 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 30809d03-c328-340b-81d6-bc81caba69d4 | -2.05498 | -52.16516 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62199c2e-9f18-3842-9701-ab0914b9637d | -2.05427 | -52.16961 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21950b5f-af22-36fb-90d1-2eadee79e41d | -2.04834 | -52.08702 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d01a6bad-4b27-3050-ba4a-5f8f5fd40659 | -2.04603 | -52.07766 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2993bc6-f61c-3083-b49f-4b7cbe340981 | -2.04533 | -52.08205 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bc5b1a4-1cb4-39fb-b8e4-18ecda991d2c | -2.04463 | -52.08644 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 113c7482-48d4-3ecf-ba44-becb26e0ed2d | -2.04233 | -52.07709 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c08aac9a-8e06-3337-a993-168d176e7537 | -1.99433 | -52.09218 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99735bce-78c1-3fc0-9f4d-9123cab40dfe | -1.99182 | -52.09296 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97674d78-f830-3e67-921e-795c3003f86f | -1.99062 | -52.09161 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8be94ad1-c73f-3f47-9075-aa48dae7a267 | -1.98464 | -52.08164 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8a70337-4e11-3e4e-a249-523a28bdfb70 | -1.98207 | -52.08239 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46f1d194-cf52-3f6b-b25d-93d8c2c92279 | -1.97906 | -52.0774 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7a3cde7-acfe-3132-a3dd-8f8b8f39d8a0 | -1.97837 | -52.08181 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9efce59-576c-32d8-b219-e1120aceeae5 | -1.97768 | -52.08621 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 387ea4d2-5bde-3e1c-bc04-89df67d9c318 | -1.92543 | -52.1279 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12507016-d109-3029-8688-aa16bcd6fde5 | -1.92472 | -52.13234 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7be3d49-164a-3da5-a188-338431bced91 | -1.92171 | -52.12733 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b02c77ac-0203-34b4-bfb0-e82cfd31f09f | -1.921 | -52.13177 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bb11881-b477-3b44-ba62-345a625adbb6 | -1.91886 | -52.0501 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a4c6ae0-70c5-3da5-a41b-571c7c2b9d2c | -1.91816 | -52.05445 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2eff246c-318e-3586-b5a3-3aeab70b2da8 | -1.89786 | -53.00698 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b82cf4d-f658-3768-a38d-c656f3873330 | -1.89394 | -53.00637 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3bc2015-6cb2-32dc-9e20-8ca4a1e7fc4f | -1.75918 | -52.06927 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef8b9bf7-b23b-31fe-b429-a48933ff92bf | -1.75598 | -52.31549 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbfc12b3-14a1-30d7-acc6-5de39c8d7aad | -1.75295 | -52.31034 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2eabcc87-d737-3a4a-a4b0-7ef8f7b0a2d8 | -1.74918 | -52.30976 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README51.md)
