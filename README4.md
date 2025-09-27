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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e24be33e-8b38-323d-82a9-bfacc16d8617 | -15.10808 | -42.48022 | 2025-09-27 00:11:00 | TERRA_M-M | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| c0d65130-0ea0-35a9-8456-443bb4fa076f | -5.77011 | -44.52688 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 197d3182-88d6-338c-8a16-e8b9483b4ec9 | -4.3252 | -45.28446 | 2025-09-27 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 965d44f6-01c5-35a5-81de-e64fb9a7b763 | -4.18538 | -44.27244 | 2025-09-27 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 93dc5a93-1b46-359c-9b51-01e788e7f2e5 | -3.65389 | -43.11102 | 2025-09-27 00:13:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 2745fa4c-9e30-36ac-92a7-02ef5851cb97 | -7.71456 | -47.29697 | 2025-09-27 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f54aa93d-df47-3093-95d3-360ba24332fb | -4.80897 | -46.80893 | 2025-09-27 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5262c98b-17c5-3c73-8dd7-522e8933d4c5 | -7.88246 | -44.0158 | 2025-09-27 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0fd54a0b-d631-3dcd-b973-9f1cd4c9e0de | -6.54724 | -44.14692 | 2025-09-27 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8d0ce9bc-a28f-3a05-a3b2-87cb849d2b4b | -5.79017 | -42.8263 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b69f0213-9d27-3b98-b93e-adc21c0be916 | -5.08001 | -44.87072 | 2025-09-27 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 233f0d95-7212-3074-a32c-c5c54a66aa5f | -2.96563 | -48.60003 | 2025-09-27 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 5f50f030-6b7d-32e9-93b7-725b4faf290e | -5.427 | -41.32351 | 2025-09-27 00:13:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f3bc6f9b-ac8b-3bbd-ad7f-a093c80a179f | -3.8561 | -45.28978 | 2025-09-27 00:13:00 | TERRA_M-M | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2f194e27-7887-3bc6-818c-6d104c2eb790 | -7.92417 | -43.31191 | 2025-09-27 00:13:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 9f2ec2a7-534a-3b17-8b47-dc4b10e23065 | -7.66323 | -45.98701 | 2025-09-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b37e60f0-0a9f-39af-bae4-9292388c7dcd | -8.72818 | -46.68757 | 2025-09-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f75ff277-6d38-3561-9b67-5d17bc0f5cb5 | -5.49465 | -43.08512 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 0596b055-198b-306b-be41-39a0672f5ae5 | -5.92822 | -42.95447 | 2025-09-27 00:13:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 46592263-89fe-3b48-a7f0-6d0a4e39775f | -5.30699 | -44.85361 | 2025-09-27 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ed5eabd5-c995-344c-98b9-adfa6033362d | -4.68684 | -46.44723 | 2025-09-27 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ab681623-8c6d-34d6-8bb7-835c2c7ca6ec | -6.54971 | -43.84126 | 2025-09-27 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 34755980-fff1-37d4-977b-92e1685e3c48 | -6.42477 | -43.07644 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| cfe48e9d-23f6-3e21-9f43-19705b546312 | -5.46772 | -43.08899 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7908bd16-1809-3cd4-9852-e6870a3a5a01 | -6.42349 | -43.06734 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b2f0a28b-01d3-3647-9cdb-7562bacac180 | -5.5458 | -45.05222 | 2025-09-27 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e561154c-00e7-3f33-86ae-ffe5cb3916d5 | -6.20954 | -42.85812 | 2025-09-27 00:13:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 47902a6a-910c-31c4-b5b0-1ddd6d64038f | -4.17902 | -44.29126 | 2025-09-27 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3df8565c-117c-318d-9310-1ad4b0c8f125 | -5.3148 | -47.2234 | 2025-09-27 00:13:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 1dd238ac-feca-39e9-8ea7-4fdfdefb3bfe | -5.45647 | -43.07786 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d191c79d-d0a4-3aae-9da8-552c479fd12a | -6.96065 | -42.30136 | 2025-09-27 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5b89946b-b1bc-31bc-8c97-a8799de012d7 | -7.55503 | -46.4085 | 2025-09-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 53ce2dcc-b1e2-392a-9b04-35ccb0bffd8d | -5.62771 | -43.37471 | 2025-09-27 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3e997bc2-55ca-310b-8cc7-52c217a1b671 | -6.06739 | -44.07492 | 2025-09-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2236075b-c94f-3f45-b707-204a3032d675 | -4.58077 | -44.0754 | 2025-09-27 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| e6b4c8ea-994d-3e84-ad0d-32bbfcc06e22 | -3.44451 | -44.12011 | 2025-09-27 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 72560d55-aa4a-3d7b-8876-0f024197a642 | -5.71439 | -42.61667 | 2025-09-27 00:13:00 | TERRA_M-M | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 56228c67-9a84-3003-935d-2ae96f34e25b | -3.45458 | -44.12772 | 2025-09-27 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c61432bd-ce18-30e8-aa46-c782a86f8b43 | -4.17657 | -44.27369 | 2025-09-27 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ced2461e-5cc8-3cff-91c5-c112aa8571fb | -4.62375 | -47.41157 | 2025-09-27 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b7c7c0ad-47ba-39c5-9448-1379ad25d67b | -7.8849 | -44.03347 | 2025-09-27 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e17a71de-27f7-3aac-aa2e-895a03e8b562 | -4.81034 | -46.8191 | 2025-09-27 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6b585bff-b5ba-37cd-92cd-7e9842fb4cf0 | -6.63755 | -40.98018 | 2025-09-27 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2d7d9aa9-51ba-32bc-92fd-8f18141361bc | -6.53968 | -43.83372 | 2025-09-27 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| cbae0fbe-e0ed-3ffc-be4a-fa82f814a60f | -7.65395 | -43.82642 | 2025-09-27 00:13:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b99dcc35-5db0-36b9-9b4c-d8cba2d71a7b | -6.75157 | -44.63417 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 1a401e83-8583-320b-a703-e4366a0786a3 | -4.93869 | -45.5932 | 2025-09-27 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7a525e5-c9c6-359b-adeb-539b7b5400ae | -5.96984 | -44.11888 | 2025-09-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 14db0b3b-3666-3971-8101-21804d9f7424 | -5.92693 | -42.94535 | 2025-09-27 00:13:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f47014ae-e318-39ba-8863-f2a83154b6bb | -6.28523 | -44.59491 | 2025-09-27 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5330219a-7deb-35db-986f-bd74520b2a21 | -6.27783 | -44.06871 | 2025-09-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 93875e94-efa8-3014-bdb0-aca33a32fef7 | -4.18783 | -44.29002 | 2025-09-27 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9f0e1f4c-1694-3bd7-a40c-c9e4e42736ea | -3.88311 | -40.43902 | 2025-09-27 00:13:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 1e96cbef-6095-3dfc-8a52-0172b3f5e341 | -7.0485 | -46.42291 | 2025-09-27 00:13:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2461899f-706d-3968-945e-2a1fe6269ef0 | -7.13833 | -45.50887 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6d5c2848-5e8d-3ad9-ad96-17ad4dd60805 | -2.49462 | -49.2696 | 2025-09-27 00:13:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4a3b1f01-7901-3c7c-8d45-e4788ed52ccd | -7.05414 | -43.02578 | 2025-09-27 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f099c693-7207-397a-85a8-2c55fd81f724 | -5.0864 | -44.85179 | 2025-09-27 00:13:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 9088f29c-e530-39bd-b5c2-8706eb0722d8 | -4.9597 | -48.01337 | 2025-09-27 00:13:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ea36075e-2e00-321c-b6a8-014becaad234 | -5.80984 | -44.88186 | 2025-09-27 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ebd4e1a-7185-3f88-9cdf-cad3eded67e8 | -5.49336 | -43.07597 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| dd4a850b-0b7c-3988-a3c0-66d12c21e432 | -3.87954 | -40.44613 | 2025-09-27 00:13:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 8330bfb4-863f-3c3b-ab09-55623c44faf4 | -4.01225 | -46.974 | 2025-09-27 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ea44b7ae-794d-3c3a-99eb-d8567e379b8d | -4.63512 | -44.06137 | 2025-09-27 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9da60b7-30ec-336c-903a-154efcad1dac | -5.72088 | -44.51329 | 2025-09-27 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52e91b37-4bf0-3bed-bebd-101d117a7100 | -4.00141 | -46.96494 | 2025-09-27 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 99.9 |
| be446315-4806-3c76-994c-17bc3c6893aa | -2.96324 | -49.09235 | 2025-09-27 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 419330cc-1271-3212-87e1-c3a514c3f29b | -7.85123 | -49.28401 | 2025-09-27 00:13:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 2ad34b5e-d5c9-3dfa-a036-5259a9b316e2 | -5.47279 | -43.06015 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| a769c3cf-5481-3ca3-935b-dc6401120b78 | -7.04714 | -46.41268 | 2025-09-27 00:13:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0c31885a-cfd6-3c91-96c3-d6262f12e0e8 | -3.8029 | -41.56758 | 2025-09-27 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| ecc0a11d-b958-34f8-970b-bca74274cac7 | -6.49071 | -43.2879 | 2025-09-27 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b4957659-e1c6-343f-afd1-a868851dff7d | -4.57072 | -44.06783 | 2025-09-27 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b714059b-7d72-3644-977a-2026abb317a9 | -5.51214 | -43.86683 | 2025-09-27 00:13:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 8d1a4325-ced4-327c-b6a8-261fccaf4c1c | -5.74125 | -44.98861 | 2025-09-27 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 88f794e8-ca8e-3ea2-92c1-2cf30dc2711a | -5.50332 | -43.86808 | 2025-09-27 00:13:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cef735b-c85e-38a6-a913-b48fe6937009 | -8.722 | -47.99753 | 2025-09-27 00:13:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d51d0e3b-6618-32ba-9f88-52d55ec95b98 | -5.57359 | -43.45297 | 2025-09-27 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d658db3f-e445-36b7-aa9e-47576414783d | -5.80732 | -42.81787 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 29.4 |
| 14f659b3-84f5-3967-a45a-884e6f5d75b6 | -5.19721 | -43.72228 | 2025-09-27 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f7784fa1-7a39-3e4b-9503-8f1b2b74373c | -6.24344 | -44.09784 | 2025-09-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4be84f36-e5ce-399e-9b72-52307ec5fd0b | -5.822 | -41.29741 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 1555c15d-7221-30ac-962a-699d57456c4d | -5.59969 | -45.36902 | 2025-09-27 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8b5b0a04-be4c-3818-a3bd-07bb68dea3ef | -5.48177 | -43.05884 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a19174bc-2f70-3895-bc55-2cfb6881f59b | -6.33647 | -43.36167 | 2025-09-27 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7f9910d1-3c83-3c15-b6d1-239d10f21584 | -2.45112 | -49.03096 | 2025-09-27 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| f4d5684a-6318-3b42-8872-6a60c24f3397 | -5.71304 | -42.60718 | 2025-09-27 00:13:00 | TERRA_M-M | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 42ec02c9-1deb-3e75-892c-f1e8f9b9853d | -4.48444 | -47.66858 | 2025-09-27 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6e6f91a2-b915-3d73-b752-f009654207d4 | -6.15717 | -43.9934 | 2025-09-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| da50d3a8-0f44-3c7e-a718-8baa0e3c3332 | -7.80375 | -46.01679 | 2025-09-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a176dddc-baf0-390f-8d2d-b95acb8790eb | -8.86755 | -47.82005 | 2025-09-27 00:13:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 58e91bce-cfe8-3f68-b095-70dcad49126b | -7.14741 | -45.50761 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5445d52d-c60a-3730-89ec-76a67314dfda | -7.04523 | -43.02707 | 2025-09-27 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| cb880101-7ed7-3345-999b-833d0cff08a5 | -4.1866 | -44.28123 | 2025-09-27 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 694a66ee-97ed-30de-ad54-96b6b39e72cb | -6.07112 | -44.85121 | 2025-09-27 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c682cf24-ea0d-319f-916c-7d531a297da5 | -6.53087 | -43.83495 | 2025-09-27 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 945ce575-e4eb-3bc0-ac2b-d60d2784b33d | -3.80452 | -41.57883 | 2025-09-27 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| abd76549-2f6b-3256-9384-8558cb5dda33 | -6.99237 | -42.39365 | 2025-09-27 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| c3cc5563-3f16-36d5-8ed1-1adc1cea7361 | -5.93287 | -43.51398 | 2025-09-27 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7c9a88be-2cd3-38e4-9340-da1046afaa03 | -5.60092 | -45.37809 | 2025-09-27 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README5.md)
