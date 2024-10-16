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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21cb766a-6729-3092-8a4f-d6ae37f22980 | -7.58327 | -42.00895 | 2024-10-16 04:06:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 63f8b077-c127-3e2d-a3ab-20498c2bb326 | -7.55016 | -42.23994 | 2024-10-16 04:06:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bc0ad716-2b89-3391-9055-7dcfb2c7c194 | -8.37349 | -41.25854 | 2024-10-16 04:06:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8f6f637-580c-32a6-8d31-3c3e8cca9146 | -8.31571 | -41.24253 | 2024-10-16 04:06:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9357de0-3f85-320a-b238-282b289e5923 | -8.18785 | -41.0033 | 2024-10-16 04:06:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 4bf30b80-84ef-3916-be4e-6b0a0a0da5ac | -8.18451 | -41.00277 | 2024-10-16 04:06:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 24fccd66-ea3a-3dc5-84fc-a41e1992d567 | -8.11274 | -42.03957 | 2024-10-16 04:06:00 | NPP-375D | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| edbfc01a-931b-3529-9fbd-70258ef68453 | -8.09493 | -41.00679 | 2024-10-16 04:06:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ffa56646-bb5a-3d76-bc1a-c4db680b1b11 | -8.16851 | -42.98762 | 2024-10-16 04:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4722c1db-0f18-3cc8-8071-58872e293cd3 | -3.46291 | -44.1661 | 2024-10-16 04:06:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6df0adc-4be6-35e5-a2de-8bee08499a3a | -3.46007 | -44.16728 | 2024-10-16 04:06:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c510470-0ba8-3720-aafe-6ea537ec2628 | -3.51437 | -43.25239 | 2024-10-16 04:06:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1e7bb6f-fe12-3f59-8af3-a0ea3f1cb159 | -3.51374 | -43.25629 | 2024-10-16 04:06:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1b14d57-e106-30aa-a9a3-022dc537191d | -3.51086 | -43.25183 | 2024-10-16 04:06:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ed92931-084b-30a5-bc5a-008646462ffe | -3.51023 | -43.25573 | 2024-10-16 04:06:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f3af1da-ec13-3226-9e58-1adacc106652 | -4.97316 | -44.6126 | 2024-10-16 04:06:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a7b3896-e91e-365a-abd6-eed373c43abe | -4.97018 | -44.60754 | 2024-10-16 04:06:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c3bc106-212c-393f-ac64-4a7b525dab57 | -3.96664 | -44.05338 | 2024-10-16 04:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 094dcd05-b211-39b4-8585-3817c65cfdec | -3.963 | -44.05281 | 2024-10-16 04:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21287dd1-e716-3081-9bfb-fa8055daaf40 | -3.79982 | -44.04719 | 2024-10-16 04:06:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76ee5aec-159d-345b-8a1d-a47181dd02f8 | -4.00854 | -43.25231 | 2024-10-16 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e86ed0a-4664-3a44-abf2-e47c18a8218b | -4.00793 | -43.25618 | 2024-10-16 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d35ff297-687c-32dd-98ed-d392298bb7b7 | -4.00731 | -43.26007 | 2024-10-16 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa0d0136-8423-38ad-a187-b94922bc4a64 | -4.00504 | -43.25175 | 2024-10-16 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b923f92-ac68-399b-bccc-0fefb03cbccf | -4.00443 | -43.25562 | 2024-10-16 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c3e695d-3113-3066-a10d-0abfc4b87bd3 | -4.00381 | -43.2595 | 2024-10-16 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8a8d54f-9ee1-399e-bf12-fa51d5ca85b2 | -3.79477 | -43.23524 | 2024-10-16 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b161c15c-8d37-35f9-b3b1-8f9251d9fc6f | -6.50225 | -44.14331 | 2024-10-16 04:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| be3c995b-e21c-3da2-9368-0f71c5bc0af8 | -6.5016 | -44.14724 | 2024-10-16 04:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9c5808ea-20a1-381f-831b-b39f3a5dea76 | -6.49933 | -44.14396 | 2024-10-16 04:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2799fdc7-c0b5-37a7-aed6-8e12eee68bda | -6.49871 | -44.14269 | 2024-10-16 04:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 83542b93-6c1f-3ef4-8a0c-4aca89a1a930 | -6.4987 | -44.1479 | 2024-10-16 04:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6cdc2fc4-0740-3943-b1bb-f84a47864080 | -6.49806 | -44.14664 | 2024-10-16 04:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8078c5a1-2b94-37e7-a47a-0508df8ff97c | -6.36801 | -44.63717 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a905e58-0487-3f62-840b-bdf70716104d | -6.32446 | -44.28689 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 98548700-51df-311f-8dd7-b7e5081a0d31 | -6.2464 | -44.6063 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33533a4d-1540-393d-bcaa-2345ceeef7b3 | -6.18864 | -44.52462 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb4a7a8b-7787-3414-b4a8-b7789cf99b61 | -6.18501 | -44.52405 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 86ff5f3b-a8b2-3087-8a3e-8c3a5e865032 | -6.18435 | -44.52811 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 19d3f4df-2b1a-3720-8583-fe2f8e95e847 | -6.18366 | -44.53234 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b7b84a85-f89b-33cd-94c4-ae68092b7826 | -6.18138 | -44.52349 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a4c39d22-5f43-3adb-8771-8b7781f5516e | -6.18072 | -44.52755 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5fc4a811-d747-3841-b85c-6069bcce0b57 | -6.18003 | -44.53175 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ec55affd-6b2a-3b42-8340-14f0df092c16 | -6.12756 | -44.60149 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f052e21f-0b96-31b3-8d68-9e9e41b97f1d | -6.1231 | -44.92858 | 2024-10-16 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14e2f2e0-be23-35cb-a84f-a76f935391ea | -6.12238 | -44.933 | 2024-10-16 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce2d5e33-b24e-3ece-9656-185d823575d3 | -6.11005 | -44.59426 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d2c9442-5581-372a-bcfb-5fc586ad9e2b | -6.08585 | -44.7016 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 042a21d6-cede-338e-baa9-205ad9d68e1e | -6.0661 | -44.70742 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3ad690a-3076-3c77-a134-e61e8232c8e8 | -5.9328 | -44.53752 | 2024-10-16 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4891066-c70a-3509-b67f-813f4e84991b | -5.90355 | -44.62431 | 2024-10-16 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7c3aa87-56f1-31cd-a64e-7db6f5b6aa6c | -5.90339 | -44.01167 | 2024-10-16 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82bf7551-e682-3847-a4e6-fdb0bf2d1122 | -5.89984 | -44.0111 | 2024-10-16 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bec40b5a-d935-3889-aa6a-29d3003e340a | -5.7199 | -44.49285 | 2024-10-16 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f72d6f84-e700-305e-8a24-fe59cc78cda5 | -5.69805 | -44.48931 | 2024-10-16 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f532efa-193e-3026-864d-f0e526136741 | -5.68728 | -44.48931 | 2024-10-16 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08bd3580-8454-3ee9-8a30-da732c56372a | -5.68713 | -44.4875 | 2024-10-16 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e458b34c-3137-3877-933a-803c0ddb2fd2 | -5.68643 | -44.49171 | 2024-10-16 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43986ed4-f234-3258-bc2b-aab2482b44a8 | -5.58254 | -44.88152 | 2024-10-16 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 66e19a62-c9ed-3d0a-8352-ecc73b6a3538 | -5.57881 | -44.88088 | 2024-10-16 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80e6af0d-52a8-3672-939a-11024fcab7df | -5.47198 | -44.68448 | 2024-10-16 04:06:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80bce900-f6ab-35ec-8595-d61533963df9 | -5.46828 | -44.68393 | 2024-10-16 04:06:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24c4123e-2b31-379c-928a-a64de4d5512b | -5.44514 | -44.80146 | 2024-10-16 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bdd5a3e-ff77-35c9-90cb-5779e4f30aaa | -6.98042 | -44.68235 | 2024-10-16 04:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ebeed78-6f33-3918-b4e4-d22cd4415b3e | -6.97972 | -44.68661 | 2024-10-16 04:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c64158d1-0068-348e-8cf6-864130fe36ad | -6.97818 | -44.67342 | 2024-10-16 04:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f86f9a8-7656-34d0-a10b-b755b5440de0 | -6.97778 | -44.72086 | 2024-10-16 04:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b66fb92b-90b8-36b5-82b1-656de394c5a9 | -6.97679 | -44.68181 | 2024-10-16 04:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d2a0038-51b9-3068-885f-bcc3ee12d594 | -6.82154 | -44.67137 | 2024-10-16 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 727c1705-024b-35c3-9ac7-60cd39487fd6 | -6.81798 | -44.46595 | 2024-10-16 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9ff4435-fd15-311f-b464-97f81a32ad5f | -6.81371 | -44.46946 | 2024-10-16 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c11af05-6573-37d3-b567-6d56931de245 | -6.81012 | -44.46886 | 2024-10-16 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ca63c1e-177f-38ca-a094-1ab769cb57fa | -6.76254 | -44.73553 | 2024-10-16 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5ec147f-bf8c-3ba6-b005-135e2a2ff1ee | -6.68689 | -44.07526 | 2024-10-16 04:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24f187e9-89b2-3de4-9f5a-c6e3188365dd | -6.68336 | -44.07468 | 2024-10-16 04:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae02e2de-9fbb-3f16-a019-9ea47028f849 | -6.67429 | -44.70557 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86e5e992-f786-3f55-9b91-aaa6decbd9d7 | -6.6736 | -44.70977 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9c327c4-04a8-3989-a956-0c775a6be663 | -6.559 | -44.19758 | 2024-10-16 04:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d4811284-6d68-3010-b8a9-f3522ab592c3 | -6.55367 | -44.46363 | 2024-10-16 04:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c35df60-4743-3ddc-9c97-ebdfbb08393a | -6.55267 | -44.46443 | 2024-10-16 04:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b953dac-099d-372c-bc5d-2757d89f10a5 | -6.53638 | -44.42801 | 2024-10-16 04:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27bb30fb-4165-3389-b9bd-4e25cf8995a4 | -6.53344 | -44.42342 | 2024-10-16 04:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 837aa1af-7fb4-3bc4-8b6f-a8e14186f3d9 | -6.53279 | -44.42742 | 2024-10-16 04:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1e79790-9c5a-337a-b5c0-825731f497ff | -6.52985 | -44.42281 | 2024-10-16 04:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6860cb4c-5d54-3ca5-b7c9-8036670995ed | -3.58729 | -44.91639 | 2024-10-16 04:06:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a785126d-8884-39ca-b822-a740e3b92f03 | -3.58652 | -44.92109 | 2024-10-16 04:06:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 015a9c3a-28a4-3979-943f-b520eb27954b | -3.4067 | -44.55526 | 2024-10-16 04:06:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7846b15a-5a73-3767-acff-72f721047934 | -3.40619 | -44.55725 | 2024-10-16 04:06:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 349c0b59-3d49-3b7f-8ece-7f1f3271acbe | -3.40596 | -44.55978 | 2024-10-16 04:06:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b13cc42f-4da4-333c-8718-f540f5856070 | -2.88511 | -44.36437 | 2024-10-16 04:06:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e979abf-2d09-3ad8-8f5d-f4d9b666a3c9 | -2.88498 | -44.36663 | 2024-10-16 04:06:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3adba73-2d4e-3a1b-a887-81e5360b611b | -2.56181 | -45.41626 | 2024-10-16 04:06:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb6d1015-5334-350e-a7a5-e2e73fa39898 | -4.86804 | -44.80622 | 2024-10-16 04:06:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c88017f-b49e-3056-b629-f4ec7d0a8ede | -4.45074 | -44.83272 | 2024-10-16 04:06:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90c002ae-5b6d-368e-b139-e3ec135d28b1 | -4.44772 | -44.82753 | 2024-10-16 04:06:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e7d60f6-104b-3453-91e0-7dd32ec5522e | -4.44697 | -44.83209 | 2024-10-16 04:06:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9a09587-0464-36d5-9f6f-3150cae6bbd7 | -4.44395 | -44.82691 | 2024-10-16 04:06:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2b77ff5-c7fe-35cb-b676-7804b416b7b7 | -4.4432 | -44.83146 | 2024-10-16 04:06:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0805bea6-7385-3f42-a50b-de9db785d5dc | -5.05999 | -45.58232 | 2024-10-16 04:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31eb4c4f-91c5-35a4-a527-2a4df837703b | -5.05917 | -45.58737 | 2024-10-16 04:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README32.md)
