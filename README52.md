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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd1416e7-1858-3480-bbf5-9727d10c14b8 | -7.13955 | -44.38434 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 160588f2-679e-38b6-9b71-68796ff2d46d | -3.01249 | -45.37977 | 2025-10-16 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 433acbae-9b2e-3bc2-995b-dcd222352c1a | -2.88333 | -50.73936 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 578d8fb7-55de-3b78-bf04-5bc6072ae388 | -5.35515 | -43.75032 | 2025-10-16 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9cb12d07-ba5b-3276-872b-33e9c39e117e | -8.18707 | -43.32206 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 849b1ea2-24e2-369c-8c51-4086c9ab09b2 | -6.18079 | -43.43557 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1946b1a7-65cc-3f66-a45a-824863f26383 | -2.38468 | -47.70797 | 2025-10-16 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad4f5eac-1c9c-30d0-81da-75be17ecb59f | -6.32731 | -46.3256 | 2025-10-16 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53b4838d-3291-3718-b05e-577bb5ae0451 | -5.87911 | -42.82451 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 68c9a4a2-9d8f-365e-80e3-0e14e9ff8bb7 | -3.13883 | -50.21242 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b1d836a-615c-30fb-a465-5143a9ddcc05 | -5.86495 | -43.87646 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6004816-c362-3d18-832c-2db0739fc739 | -5.85218 | -42.88659 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d03b57d-ac40-3232-8bd6-830afbeb078c | -4.89222 | -48.58572 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72ac843a-0e17-3856-9e6f-08cb50808212 | -6.10157 | -40.88842 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 9fde76ff-93a8-3365-9726-d569814c04d5 | -2.12635 | -48.03553 | 2025-10-16 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3fb327b3-ef23-3f04-a99a-a9b96d69320b | -6.49351 | -47.22743 | 2025-10-16 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| affc1fd4-b51b-3ff8-a309-46d11a700b14 | -2.70561 | -49.87098 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a3ae05d-054d-3f35-b013-19cfaece1d21 | -8.06424 | -45.42208 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b64ccc9f-f882-3624-bc70-d45ecc1836f8 | -6.19752 | -44.1051 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 092bfb84-1cad-37c5-aa3d-a697ba67304d | -7.28451 | -41.95434 | 2025-10-16 04:38:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bb22f9b0-9c68-3dee-8a08-9b7444d9ce55 | -4.12278 | -50.72236 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b97de84c-186d-38b7-a332-210fa2f2d279 | -4.86589 | -43.40088 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ab6816e-d6fd-3329-a1bc-82ecdc188553 | -4.8026 | -48.72284 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2430ee6-f4d5-378d-bac9-423d368c3f5b | -3.38896 | -50.27006 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b88f69d1-2e35-3480-93d6-66397a521c2f | -4.87238 | -48.71318 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7434935b-8095-32a5-9a81-bf5958255b5c | -3.86609 | -50.04907 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9a361d4-2158-37fc-8a7e-9f45c7184905 | -8.21445 | -43.99103 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e354d4cf-34a1-3081-8ab5-a56be6e5f41c | -3.0839 | -49.48099 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63b851ed-92da-35a9-8dfd-c2795d65111a | -8.29344 | -43.4294 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1f8cfe69-14c5-39f9-9f32-854c5437772d | -4.11184 | -48.02361 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ba36cadd-dcd4-3273-a941-85adc1324b68 | -6.32304 | -44.71279 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c611a1a6-6d84-35df-b2cc-3642d23039da | -5.63484 | -43.294 | 2025-10-16 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b47a4d1a-dd55-3c87-94fe-91d36334900e | -5.74225 | -44.98571 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98ae7054-ca7d-3084-896c-a63197dbc168 | -6.13347 | -44.28701 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a087633c-c662-3cbf-86e5-48b77123b8f6 | -5.86382 | -43.88417 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f50a978e-57a8-3dba-afbd-6377e680d94d | -6.97631 | -43.82104 | 2025-10-16 04:38:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0ce726f-da72-3d8e-91d3-c6a2cf3861dc | -6.12892 | -44.28997 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34b9760b-6307-31ed-a1c7-055b61d6e432 | -4.77877 | -43.92691 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f3a15ef-108d-3e9b-a4cf-9e28f94cae5d | -3.48877 | -50.08773 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad2c3c0b-94d4-3fd9-a579-5213fa5ed364 | -4.92609 | -45.89925 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efefd581-5a28-3acb-919b-c4ebde27e91e | -4.7635 | -40.86329 | 2025-10-16 04:38:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ced17580-a4e6-3600-8d60-59dbec445a79 | -5.4717 | -42.934 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e9f544a2-ba77-3d7c-a411-5e85d19c1cef | -4.65338 | -44.0956 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 027f89f9-5987-3dfa-ba48-c3412053d915 | -4.50053 | -45.39586 | 2025-10-16 04:38:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59fb618c-54ba-384d-9ead-6fcd4b44ac19 | -2.87018 | -50.73349 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 34d0e8cb-f717-3bed-99e2-f2a3cd4dabda | -4.1157 | -48.02066 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5d1ba7e2-6b06-3bdf-ac5f-fbe6bd5a2ac5 | -5.17042 | -46.41029 | 2025-10-16 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ec3026b-b900-3f71-8016-53961fc91f99 | -3.84712 | -49.93059 | 2025-10-16 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 138d950f-0f2c-384f-82bb-fc17880c9034 | -8.24693 | -44.13178 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d31e69fa-4d18-3b0e-a5a4-f4f49b83dcfc | -4.781 | -46.61313 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad6985eb-f6a1-3da2-9419-23e68a45de1d | -4.35704 | -45.53068 | 2025-10-16 04:38:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66f34731-affb-36c3-9301-e662c70ea788 | -7.47561 | -47.02256 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d69d2eea-e483-35cd-8c49-5a4a0972468d | -4.83935 | -42.79408 | 2025-10-16 04:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| f0cff788-d1d3-3f57-b918-3b20c513f520 | -8.24358 | -43.33257 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0bb8c390-931d-3631-aff0-9a922bbe01be | -4.80814 | -43.20913 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b2cf4eea-e316-365e-8684-95c07d8cdcf0 | -2.71065 | -49.86088 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bd4aeb16-8223-3c1d-854a-d2d4c8735a7f | -8.21548 | -43.3132 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| db1a9f7b-c3cd-3830-abcd-7f3246d84037 | -3.14424 | -49.03088 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84b1d3c4-a27d-309e-be74-572592662da9 | -5.46952 | -51.17817 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03a60b2b-b4bd-3e17-997f-e7879cfdc168 | -4.66746 | -44.08361 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15b9163d-718e-3e98-b706-908c16c58baf | -6.14995 | -46.15721 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 074a9b56-f716-3fc2-a6b5-ad681835f8ba | -6.06022 | -41.89043 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e13003a0-7f57-323b-8175-cdb01db78707 | -8.24379 | -44.02776 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d210024f-fde8-3846-8fbd-518ef1fcd1f5 | -7.66595 | -42.38168 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 9b2107ea-0246-3599-b675-501ebeb696ec | -6.19343 | -44.10455 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 319d606c-9480-370e-9395-f398bc386ee3 | -4.82902 | -45.6528 | 2025-10-16 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 352a6362-775e-34ce-a242-d88d6fb05e40 | -7.01082 | -41.95285 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6b2ccbed-f27a-3f4e-8c87-2ea599ba48d1 | -6.40982 | -42.55226 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a1dd9724-81be-3176-8608-f38e3ff34d8f | -8.18757 | -43.96666 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cd1dba8-db9f-3a51-94ee-8b7af70c8e13 | -6.69186 | -40.86505 | 2025-10-16 04:38:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5375aa7a-52e1-3927-888a-a63696c23a8f | -2.93877 | -40.09598 | 2025-10-16 04:38:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 09810693-f2ef-3424-820c-8d36446bd903 | -6.75432 | -44.37067 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5bd3b57f-5fc6-3125-a0fe-4b13035619f9 | -3.13209 | -50.2114 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 52e812b6-aae5-3d2b-946c-73109e479d1b | -5.33193 | -42.90571 | 2025-10-16 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ca677645-0381-3e71-b8b4-cb3542d9cbfb | -8.25491 | -44.105 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9d504c9-c4b4-319d-91dd-f236494932e1 | -7.48056 | -42.67251 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8cecb165-8fed-3514-bedd-31f2e6d56358 | -6.44723 | -43.38245 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4eddc909-be6e-3921-9caf-f699f08066b6 | -3.47487 | -50.02385 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9acb8364-5b8c-3932-9dbd-cae6813d660b | -5.38623 | -48.90985 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ad7d18a-5074-3363-983b-b2a90d79e3b5 | -7.54027 | -47.38159 | 2025-10-16 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a1ea4e2-bcb0-3989-bc5c-76967bf3c689 | -4.94022 | -41.71545 | 2025-10-16 04:38:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6153ec68-a083-3294-b810-494cd60f1c75 | -8.29467 | -43.42056 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f419afee-320d-3a5f-87c1-cea57882401b | -5.33183 | -42.55794 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8c394438-2495-3002-adfb-59b1a1ef112f | -3.07345 | -49.50428 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 305e882b-7acc-3f2b-906d-96a253ebe4e5 | -7.48554 | -47.02812 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbf6424c-86cc-3e4c-b4e2-ab6e5d0b70d6 | -6.41406 | -43.58397 | 2025-10-16 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23c39310-f74f-3218-8fea-1efb2704f3f4 | -7.95168 | -44.13927 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1b61c210-37c1-3bae-bc01-7e61541432b5 | -6.4527 | -43.37502 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec2734c8-56cc-3b85-b5de-c1cfccd7b9ea | -7.20571 | -43.64089 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63c2f6cc-43af-323c-bdb1-4a548cb7b2b4 | -6.33524 | -44.01573 | 2025-10-16 04:38:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2c5486a1-027e-3a7e-98bb-57bfb525af99 | -5.89617 | -42.83182 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7d2d5e76-cdd2-31d3-9e1e-954828e81f39 | -4.66431 | -44.10439 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 143e18ae-24dd-30e3-9275-191f24b773e6 | -2.05078 | -48.79905 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0959c3c2-4197-3612-98d8-4a01ecc5881c | -3.8829 | -52.07523 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8acc58be-0fa6-3f5b-a721-13773fd8b85f | -3.43812 | -50.25542 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff1c3a5e-a503-3a41-a345-cd9ce07cc6c6 | -7.46723 | -42.66782 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b5b0a675-fc30-3f3a-bebd-c09885ba302a | -5.63874 | -45.97075 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75a272cb-d124-34e0-b8e9-ecb04a7cb1eb | -6.1284 | -44.2935 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0899a613-dda3-3c98-9a1c-1c641b2d1af9 | -8.25449 | -44.07685 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b54a00c7-aece-3fc2-a128-45fd6ee19447 | -7.49518 | -46.65156 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README53.md)
