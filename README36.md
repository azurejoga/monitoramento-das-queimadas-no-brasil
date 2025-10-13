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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd667c50-c73b-393f-bdab-7ee9771171e6 | -8.24022 | -43.34455 | 2025-10-13 11:38:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| a58b42eb-b2b5-3413-a00c-81e5a64d89cf | -9.32818 | -36.86888 | 2025-10-13 11:38:00 | TERRA_M-M | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 6.9 |
| aa4fbae0-f833-3c37-97be-4b209a9c3c51 | -9.38467 | -45.7274 | 2025-10-13 11:38:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 4bac5508-9d20-3e76-9102-d5e1b51199dd | -9.85246 | -40.25414 | 2025-10-13 11:38:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ef84256d-4f93-3e00-83cf-2eda64c3a280 | -6.52583 | -38.7201 | 2025-10-13 11:38:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a09ceb38-a661-3fcd-989b-188f91a17d90 | -11.28154 | -39.51723 | 2025-10-13 11:38:00 | TERRA_M-M | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| ad261c45-43fa-3a99-910e-68e994fc6cc6 | -8.22834 | -43.34276 | 2025-10-13 11:38:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.5 |
| bf36bffa-5619-33a7-97e1-25a8251c3111 | -7.49968 | -44.61496 | 2025-10-13 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 6a11fcfd-69da-389b-9a15-66a73b4eb515 | -7.77228 | -44.72125 | 2025-10-13 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 201.8 |
| 39b355f7-e4ff-37aa-96fa-3316420ef90f | -8.8928 | -45.3591 | 2025-10-13 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 7f0437ff-ee0d-3e8a-a521-01ab667a207b | -8.90275 | -45.34228 | 2025-10-13 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 79dea3e2-2964-3914-a04a-cb1ed1f94c91 | -7.48278 | -44.63511 | 2025-10-13 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 4f092786-d9c0-3749-bc23-3b23fd5d67c7 | -7.64746 | -42.57053 | 2025-10-13 11:38:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 4ffb9082-02f1-3d65-8b67-132c5bb4fc1c | -8.21647 | -43.34095 | 2025-10-13 11:38:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| c6fe1dc1-b6ca-38db-8048-4f5f35b341b0 | -7.37553 | -44.07209 | 2025-10-13 11:38:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 15508203-2f65-3ebd-beb9-ec2f76191834 | -8.88047 | -45.26036 | 2025-10-13 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| bbf1987a-29ef-398a-96c1-c54fb759dc8d | -7.48635 | -44.61282 | 2025-10-13 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 302.9 |
| 00df681b-cf10-3788-bf68-b1fb37fa5123 | -6.6105 | -38.71003 | 2025-10-13 11:38:00 | TERRA_M-M | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 4e9abb36-046e-3109-9661-b4d52423c251 | -7.75535 | -44.74133 | 2025-10-13 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| a91d4835-75c8-3a1a-92f7-6301697e936f | -7.49619 | -44.63687 | 2025-10-13 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| dbc77893-ec5c-3e04-b937-f4ba6f3c101d | -8.88715 | -45.26727 | 2025-10-13 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 38.4 |
| e2ab196d-13ae-3d84-9da2-58705eb02113 | -8.10398 | -39.47193 | 2025-10-13 11:38:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 68bd62cc-7cfa-35ec-8cf0-eb842744631f | -13.08432 | -43.04411 | 2025-10-13 11:40:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| fe470b50-4bd8-3514-8164-ee1a495a4d23 | -11.8717 | -42.91653 | 2025-10-13 11:40:00 | TERRA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 40be0a37-7398-368b-8bf8-cdbe2b48ee6c | -13.5194 | -42.30814 | 2025-10-13 11:40:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 397200cb-ba99-3291-8156-7bf7dd56a9cf | -13.01679 | -43.02587 | 2025-10-13 11:40:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 710f6b4c-0479-3c3a-addf-3cbba390e644 | -13.00618 | -43.0241 | 2025-10-13 11:40:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 2e2bd453-2c94-370d-a22c-1b148c1bdbc5 | -13.15205 | -42.55307 | 2025-10-13 11:40:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 40.1 |
| f25d1e05-c5e4-3a58-8873-5b0cade2b918 | -14.03641 | -41.50248 | 2025-10-13 11:40:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c4750cdd-8ff0-319e-a0f6-f55eb81ea057 | -13.44576 | -47.69598 | 2025-10-13 11:40:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ddc90dce-e4b2-325d-a491-ecd399b4bc0d | -13.15401 | -42.54074 | 2025-10-13 11:40:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| e7dcf385-9dec-3fcc-8fa6-de447bc24717 | -14.30892 | -42.69804 | 2025-10-13 11:40:00 | TERRA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 5c9fb7a0-b29a-358c-b290-4bd920855b21 | -13.73938 | -41.53816 | 2025-10-13 11:40:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| c64d785a-8380-3cb3-9e12-5a4ab488e3d5 | -13.66451 | -42.88076 | 2025-10-13 11:40:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 6ba193be-bbbc-3b2f-9eaa-bd8703bd5f41 | -13.44835 | -47.69049 | 2025-10-13 11:40:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 7c20b21d-7d6f-3273-8c24-ec7a04bb38de | -12.75149 | -42.68169 | 2025-10-13 11:40:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| debcb402-ebf5-3547-87a5-0a8a25cb94b1 | -12.75347 | -42.66936 | 2025-10-13 11:40:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 0dee36d8-4d05-3da0-9810-c256ea0d8f9d | -13.71579 | -42.49301 | 2025-10-13 11:40:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 42ca44e8-c2c2-3468-b3fa-f49ca235fbba | -13.42099 | -43.67727 | 2025-10-13 11:40:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 111b5609-2e0d-3bd0-8d19-2e7b89db34a9 | -16.50926 | -43.3756 | 2025-10-13 11:42:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 701edf50-8b57-3cde-b3d5-71dd7cce2020 | -15.79449 | -43.10835 | 2025-10-13 11:42:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 22.3 |
| a87faad6-5a9b-3ce6-86e1-0ca92eff5499 | -17.28396 | -39.7873 | 2025-10-13 11:42:00 | TERRA_M-M | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 41c0aa7e-3915-3f41-93b0-700f4bf7b282 | -15.85771 | -42.89999 | 2025-10-13 11:42:00 | TERRA_M-M | SERRANÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3166956 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4118c0b7-bbd3-31bf-acaf-9dd687605684 | 1.9134 | -55.7024 | 2025-10-13 12:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 5b10f31f-5b4d-3bd0-81fd-c20172af7a5d | -12.7798 | -50.6834 | 2025-10-13 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 3a976ace-628b-31c5-b275-8efd0f3ed36d | 1.9134 | -55.7024 | 2025-10-13 12:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 985b5daa-70a3-384a-8bc2-96f90a672dce | 1.9134 | -55.7024 | 2025-10-13 12:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 0bafaf7a-02e5-3e31-8a87-f59c70e12c1e | 1.9134 | -55.7221 | 2025-10-13 12:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 634aa998-4bbd-39eb-ae46-c3d074588c7d | -13.4596 | -51.2827 | 2025-10-13 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e2a8d994-47ff-38af-b42b-462e0924be63 | -12.7798 | -50.6834 | 2025-10-13 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 1384d66f-15e6-3194-add3-f43b2fa8ea56 | -13.4596 | -51.2827 | 2025-10-13 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 5efba8fb-45c7-30ed-a73b-1120c0ce0bfd | 1.9134 | -55.7024 | 2025-10-13 13:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| a24d85d5-5740-38d0-b58b-380777f8b044 | -15.8085 | -43.7838 | 2025-10-13 13:00:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 104.2 |
| fdcd4ad7-d9ce-3fd3-a5b2-69832f4188ba | -12.7798 | -50.6834 | 2025-10-13 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| ace4b32a-5ed3-3b45-9149-893c7b5bae9f | -17.3384 | -53.7922 | 2025-10-13 13:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 126.5 |
| f8578c82-99eb-36c8-8ff1-94c84e270a54 | 1.9134 | -55.7221 | 2025-10-13 13:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| a3dfe005-e9d0-3d70-bc60-ba07553a5b91 | -17.3183 | -53.8163 | 2025-10-13 13:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 38102855-2f9d-35a8-b05f-153b1ee97385 | -13.4404 | -51.2851 | 2025-10-13 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 5c18ef42-7ca8-3d50-942b-43afdcfa3d1a | -14.2639 | -51.4982 | 2025-10-13 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 191.8 |
| 8462f71e-8ac6-3c1d-bb98-209b8ee9cbbd | -13.4596 | -51.2827 | 2025-10-13 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| daf4f372-0c59-31cc-a5bb-af9857e16e3f | -13.4404 | -51.2851 | 2025-10-13 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 24285c1b-6039-380e-bc68-236640eb5981 | -15.8085 | -43.7838 | 2025-10-13 13:10:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 0e27bfeb-4e55-3797-997f-d1ae45ba91a4 | -14.206 | -51.5059 | 2025-10-13 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 3844d147-35ee-3548-b9ad-b67658322d80 | -12.6954 | -51.1855 | 2025-10-13 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| bda74ad4-94fd-3779-a956-4d5d2ecfde8b | -12.7798 | -50.6834 | 2025-10-13 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 8ca1c8bf-7ee1-32cf-951d-0fa0dba0ab04 | -14.2253 | -51.5033 | 2025-10-13 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 954cdc92-7b0d-39bc-badc-feaee48ea0d1 | -14.3015 | -51.5573 | 2025-10-13 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 03235bf5-ae34-382f-8569-09db83345c1f | -14.2632 | -51.541 | 2025-10-13 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 1ef658b7-ede3-3eb4-900d-29778bed8051 | -15.3357 | -43.8337 | 2025-10-13 13:20:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 136.9 |
| fcc399ea-1abd-35a3-9357-dc11f059d47d | -12.7798 | -50.6834 | 2025-10-13 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 21c2a7cb-5aa3-3d82-a8df-2f359c337d39 | -13.4596 | -51.2827 | 2025-10-13 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 123e5b76-e205-34c0-877f-cf1d1ebc4895 | -13.4404 | -51.2851 | 2025-10-13 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| a1ac3101-8861-3492-87a3-c30bec1d3337 | -12.6954 | -51.1855 | 2025-10-13 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 7a03a424-d0da-342a-82a9-2520ac0ae704 | -12.7798 | -50.6834 | 2025-10-13 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 9f75be6b-0c63-3725-8da0-022cffe57bc6 | -13.5362 | -51.2942 | 2025-10-13 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| c79efb38-8281-3f45-9e80-035290959416 | 1.7851 | -55.7831 | 2025-10-13 13:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c158ac24-62c6-3e31-84cb-895e88733905 | -13.5359 | -51.3157 | 2025-10-13 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 0f167f8f-0d8c-331b-b7e5-73ded1d6b4d8 | 1.132 | -50.9359 | 2025-10-13 13:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 73.5 |
| b174d9cd-ba41-3444-b587-6141dc680690 | -12.7606 | -50.6857 | 2025-10-13 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6b0ead83-ef0f-36a0-b2bb-622c83b0189c | -12.6954 | -51.1855 | 2025-10-13 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| d313f603-ce7b-369a-b198-ed8f3c577257 | -12.6762 | -51.1878 | 2025-10-13 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| a4d6d719-4990-3c6a-b2f9-c99143fd1631 | -12.2383 | -51.1332 | 2025-10-13 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f48278d0-ec10-36db-9a79-c07d8922497c | 1.9134 | -55.7221 | 2025-10-13 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b6be9293-dd87-34b4-add4-525284b525c2 | 1.7851 | -55.7831 | 2025-10-13 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b261fe07-1b59-32f2-b49c-05f96e3d0e0f | -12.6954 | -51.1855 | 2025-10-13 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| ac5dfe2e-fabc-3e6c-b969-ab170b3b39f3 | 1.132 | -50.9359 | 2025-10-13 13:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 87.9 |
| d4df3c10-efd5-3742-afe2-ae7e58caa111 | 1.8034 | -55.7829 | 2025-10-13 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0b50dca2-b42e-3361-a47d-9b68271d49b2 | -12.6954 | -51.1855 | 2025-10-13 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 488de2b0-76a4-33d8-b5af-5cdf9cbd86a0 | 1.9135 | -55.6629 | 2025-10-13 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0739e337-f3b1-36e5-9c70-920c1b53b6ef | -3.6135 | -41.6328 | 2025-10-13 13:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 139.3 |
| 6613d78a-8396-3b5a-8201-addcdbbcee74 | 1.7851 | -55.7831 | 2025-10-13 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 9a3b2000-9e8b-3307-aa3e-2c4b2368dd5e | -13.517 | -51.2967 | 2025-10-13 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 37b77198-6c49-39cc-8033-5b737de501b6 | -13.5359 | -51.3157 | 2025-10-13 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 136a2f9b-4473-3077-8d91-fe1a5ccb30ee | -13.5166 | -51.3181 | 2025-10-13 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 3f7020be-9c1a-3328-838c-2d6ca5fbf73a | 1.9135 | -55.6826 | 2025-10-13 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 74cf2bc2-1fde-3324-8765-014aadd8c99e | -12.6762 | -51.1878 | 2025-10-13 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| fd9116f2-74da-36db-bc36-ae33f0920d06 | -12.7798 | -50.6834 | 2025-10-13 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| b53d9898-52bc-32bc-a8d9-1a936feb6f9c | -12.2383 | -51.1332 | 2025-10-13 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 2ea63c40-f7c5-3d40-b13b-61b0d1727eac | 1.1504 | -50.9149 | 2025-10-13 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 04db28f1-aea2-325c-abc9-8426aa2ddb58 | -3.6135 | -41.6328 | 2025-10-13 14:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |


[Clique aqui para ver as próximas entradas](README37.md)
