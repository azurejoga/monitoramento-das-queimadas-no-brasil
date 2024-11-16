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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 676a826c-30d5-343d-90ed-3f6c5236f4ab | -17.57118 | -57.46061 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 265c5baf-772e-307c-aff5-13d4a18bf78e | -17.77694 | -57.59451 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a0f0de06-7711-339e-9cc7-f01ab6916adb | -17.23952 | -57.44679 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| a877df34-c23a-3385-a3ad-647f1017a3cc | -17.57817 | -57.4823 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c67480f8-a570-375d-ac52-7637568ff3e9 | -17.58229 | -57.47898 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 36ab9b9a-ec66-3dcd-967f-3091ec2430cc | -16.95581 | -57.63787 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 814da0e3-5ea8-3ec8-ba0b-a0ffd943bf68 | -16.02033 | -59.37417 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6730e7bc-971e-397e-9726-85101c343df6 | -17.5775 | -57.48626 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6d981f2e-0e63-32bc-aac6-06212f095bd9 | -17.61565 | -57.40784 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c8251ce1-10f5-371c-83dd-40f1937897ed | -15.90916 | -59.26706 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 81b68cd9-1c3f-31a7-bd85-918646a40730 | -17.58824 | -57.57018 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 39167dfa-e93e-37ea-9f9a-adfa2d35a396 | -17.57092 | -57.56697 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 462b3329-5c42-3fef-a344-d52615b1c0f7 | -15.89767 | -59.26468 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 8de81ba4-2da3-3a83-b929-0a7c3d23f805 | -15.47281 | -60.04951 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7f9859ab-759b-300a-bc97-d210e39244d9 | -17.68424 | -57.5616 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| c6569818-653c-3482-83b2-967a69a69703 | -17.57319 | -57.44877 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5dcc3f01-4a8a-312b-ad32-74477864bcc8 | -17.57261 | -57.47312 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fbc7b357-0a92-36e2-afa7-16beb02aea71 | -16.95513 | -57.64192 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f9c006c5-8aaa-3150-884c-784cd5c75189 | -17.23067 | -57.19102 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 49fac36d-599d-3bab-92b3-5439beeaeae6 | -17.57279 | -57.514 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 0630fde6-6ca4-3cce-a842-b0bd30b33856 | -17.2423 | -57.45139 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 27ae8246-6caa-3dc7-8390-90753bbc4a85 | -16.10058 | -60.09833 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 56422990-2249-3f34-8851-fd173040bd06 | -17.58585 | -57.50006 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| cf782e7d-d099-39fd-83a0-e1c7f0f7075e | -17.58545 | -57.56554 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a88feba9-5deb-393c-91c1-e86e9f9c6238 | -17.59744 | -57.47363 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9071b085-3442-305a-91b4-7a5f86af95a6 | -17.64207 | -57.54729 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 45f22035-cad7-39c8-888b-a37d93962a55 | -16.01347 | -59.36803 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 26d884c6-ca0c-31de-a689-45ac6be8907a | -17.57211 | -57.51797 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d40c7ac7-c4ad-3ca8-b2e1-90a45d2696d5 | -12.41103 | -54.20947 | 2024-11-16 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e73b608a-3361-3dc8-bc66-0666aa93a3f2 | -16.02123 | -59.3692 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 46d31196-0c9d-34c1-9901-c5fe51fb1a3f | -17.70298 | -57.57738 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a495468f-5d7d-393d-8660-fef9bd9f2754 | -17.62143 | -57.564 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 76ddfa8f-e9e3-3f2c-8704-60cac4cf46af | -17.68943 | -57.48895 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f69c0468-b325-331c-81d1-af90f37f4dda | -17.24095 | -57.45932 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| bffaf4b7-a0ae-3978-bd93-58e59e004d3b | -17.63594 | -57.56257 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 2f28323c-1da3-3e02-a4c0-eac4eae5779c | -17.63448 | -57.54999 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 63938716-94cc-3c4b-962f-b119f1c19039 | -17.63861 | -57.54665 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fe868e8c-f350-3420-8839-4df9ead44aab | -17.20911 | -57.23531 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 81bac082-e416-3737-8e84-21b948146056 | -17.61584 | -57.55474 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 41aafab7-7b5e-3a2d-87e0-358c0f7dfa32 | -16.09319 | -60.09308 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02752b27-be28-34a0-a381-60a2f1f178f0 | -10.03057 | -64.22358 | 2024-11-16 04:53:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 822539c3-f995-36e8-9b01-1a1d5ace49a2 | -16.09656 | -60.09752 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a382e623-14b2-3132-b607-4834258630bc | -17.23402 | -57.45805 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 3ffd537b-459d-32c8-8d2f-ae8fc9c6403d | -17.5774 | -57.46584 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| d6626a87-8031-3738-bad4-3bccae9fd6db | -10.1183 | -65.03265 | 2024-11-16 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcd24f6e-b94e-3e85-8581-7fcd574753d5 | -17.56351 | -57.44293 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d0fcc632-5a12-3dbe-a4f3-d80c23dd5159 | -17.21729 | -57.22876 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9cf4cb7a-4d9a-3534-9100-570de40be875 | -17.56595 | -57.53321 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 51d12d07-a6d7-319d-9762-fb28839eff6f | -17.54797 | -57.53399 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 8f01b2de-7c0c-3a98-86e4-b9064b15151e | -17.55144 | -57.53463 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d63077a4-4859-302c-bf88-d04165dee8c3 | -17.06942 | -57.41795 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ae015c61-4809-3d60-95dd-ebb0cbed190f | -17.56898 | -57.43173 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5c5deb82-82f2-34a3-83b8-ea9ce62b2165 | -17.57582 | -57.58021 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ba4c9d98-1934-358a-95dc-7a3bd3f16030 | -15.67326 | -59.73093 | 2024-11-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4b0730c-b22b-346c-a904-499bf0af0ae9 | -16.03825 | -60.12004 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0807a8b-f2cd-3206-b709-f6b5062fbd99 | -17.62902 | -57.56129 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 41fac1cf-00a5-3a00-8d6e-b93b78caa889 | -17.24373 | -57.46393 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b0484386-260a-3964-995e-431f2c496d57 | -17.68837 | -57.55827 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 118dc62f-4be0-3eb2-b102-815121528f5a | -17.66483 | -57.54982 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 0f04bcf1-9a64-3045-b9df-4270ed6447d8 | -17.57386 | -57.44482 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e1560865-01f4-3a13-815b-2fb56fb0d5cb | -17.57431 | -57.54705 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8cd472e7-9111-3c0d-84fb-5300b317036d | -16.93485 | -57.63399 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e96d8e71-912c-350c-8830-cdf1723c0955 | -16.01565 | -59.37154 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ebe9ffb0-4bde-3ca5-b61f-790e90abb72a | -17.6193 | -57.55539 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e7872019-c96f-3542-96fd-453d7b9c4ccf | -10.02472 | -64.22243 | 2024-11-16 04:53:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab211500-b440-3b8e-8597-6e241c11d2dc | -17.57507 | -57.56362 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bb53e334-3995-3bd1-b59a-0c1229f060ab | -17.57076 | -57.52591 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f91733ad-5213-3a1c-b70f-0253e667bbd5 | -17.55835 | -57.53591 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6c5bd1ee-9d1c-3926-ac3c-0ce50ff44adb | -17.56603 | -57.55374 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1560cce2-5990-3e6b-88e2-993dc629d913 | -17.57785 | -57.56824 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 60d2e607-3696-312e-918c-ed79f3b31463 | -17.56182 | -57.53655 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 06cb68e4-4153-310e-8fd7-3f169aae6fab | -17.59383 | -57.57943 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 0dcd4a4a-257f-395f-8fbd-16edd25b127e | -17.23131 | -57.47394 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8ac45211-4998-3b93-84a4-d8ffb7e5cf12 | -19.76853 | -55.4082 | 2024-11-16 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8e1f52b2-9877-39b9-8576-c0f3a810e579 | -29.9025 | -54.92913 | 2024-11-16 04:55:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| a5b0f3ca-c716-3985-87ee-4a7c4a44d9fa | -29.28667 | -52.01762 | 2024-11-16 04:55:00 | NOAA-20 | CAPITÃO | RIO GRANDE DO SUL | Brasil | 4304697 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9bb54226-0e1a-3b1d-a064-5f8332d912b0 | -29.89891 | -54.92852 | 2024-11-16 04:55:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 79fd4aec-1e07-3b75-ab04-e498008c4ba1 | -18.72616 | -55.58242 | 2024-11-16 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a578e792-2326-319a-ad07-e8eeb098b4ff | -28.41603 | -55.72301 | 2024-11-16 04:55:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.8 |
| f318f2a7-3054-3873-bfb1-29e358334d1e | -19.09509 | -54.77981 | 2024-11-16 04:55:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2dc30c7-9ab5-3983-97d5-d2a6032c50a8 | -19.21545 | -55.14582 | 2024-11-16 04:55:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6b3e577-c236-3a43-a841-f96dcb88063c | -19.00167 | -52.39237 | 2024-11-16 04:55:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e53561b8-4a7c-3109-b875-a8438b0c5bb1 | -19.76797 | -55.41186 | 2024-11-16 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| eed577b3-856c-3af5-a4c0-d5b497da3f37 | -19.00526 | -52.39292 | 2024-11-16 04:55:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae5290cd-0be1-34ac-a30a-5b0b6ddeca6c | -30.12807 | -51.59466 | 2024-11-16 04:55:00 | NOAA-20 | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| a71d6a29-d80c-3899-9644-4c7c1e22d68e | -20.21009 | -56.62786 | 2024-11-16 04:55:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8c63556e-381b-3a6e-bf98-abce8db23355 | -28.40012 | -51.3532 | 2024-11-16 04:55:00 | NOAA-20 | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4073958f-0292-30f9-9fa2-8fed08f6afa6 | -19.76522 | -55.40763 | 2024-11-16 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 80674d85-7880-36c8-b973-61077b68a76f | -2.78 | -48.5806 | 2024-11-16 05:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 2bd0aff0-9177-30a9-94e0-1ec53de4dbcf | -2.2299 | -53.6018 | 2024-11-16 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b6ee829e-5713-3625-9189-abf8d4193f27 | -2.0271 | -53.9477 | 2024-11-16 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| f8a563b8-08fd-32f1-9dd4-e6f8d60741f3 | -3.2008 | -45.5629 | 2024-11-16 05:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 5e4aa0df-393e-38d4-aa62-5a8d61eb5f1a | -15.9028 | -59.254 | 2024-11-16 05:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 5c133568-a15f-39bf-99f2-d276faee3aa4 | -15.9222 | -59.2521 | 2024-11-16 05:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 567e3f48-c73d-370b-be22-bea40e67e871 | -3.2753 | -45.5151 | 2024-11-16 05:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| ceb0917e-4e58-3a4d-960f-73adb859bb84 | -3.2009 | -45.5405 | 2024-11-16 05:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 42e46618-bb90-3fb0-83a4-13c0aefb9acb | -17.235 | -57.4516 | 2024-11-16 05:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 0c3c81c4-5416-38ff-a96e-b9dee5baba41 | -17.2547 | -57.4493 | 2024-11-16 05:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 123b931d-3309-3e12-8705-12fd4e0cd238 | -17.5675 | -57.5351 | 2024-11-16 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| a5e60b8e-2f35-344d-b4ab-268bcf117db2 | -2.2299 | -53.6219 | 2024-11-16 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |


[Clique aqui para ver as próximas entradas](README56.md)
