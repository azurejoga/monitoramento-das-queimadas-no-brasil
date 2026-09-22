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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed4e50b8-44c2-3d72-8de5-e8e540118722 | -6.57798 | -44.16069 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 64b8f9f2-550b-3e8e-9ddd-4ed8dffafede | -6.29294 | -47.65527 | 2026-09-22 04:02:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1bf25da-12d6-356f-a567-b8bd7836b020 | -6.6709 | -47.38091 | 2026-09-22 04:02:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8984e30b-af42-3cca-9bcb-ddee725354ad | -11.43673 | -47.33715 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8c8f8aad-0c29-3722-8a1f-9036a83593ed | -10.5195 | -44.8752 | 2026-09-22 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e771533-0d2e-3320-a346-dd53cb825178 | -5.31939 | -43.41534 | 2026-09-22 04:02:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4b3d1f9-aaf0-3c0b-8946-93343ddd0f33 | -12.14086 | -47.39791 | 2026-09-22 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 769fdf7e-d3a5-3037-befc-8be70cd3598d | -5.65331 | -43.4161 | 2026-09-22 04:02:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6d6756af-69c3-3841-a16a-4335fda8b818 | -7.52456 | -46.21828 | 2026-09-22 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 274ea6b7-441e-3122-80a8-9aab0de3ef48 | -5.82256 | -44.13416 | 2026-09-22 04:02:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ceac4d7-ae1e-3c9b-9760-dd3d3b9f3feb | -10.46225 | -51.30919 | 2026-09-22 04:02:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f28c7ecb-10ec-3dec-aca8-cb3ea7db4e5f | -11.8515 | -46.81728 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ac7c09e6-93b6-360a-bc26-fe2c6172ff2b | -5.65391 | -43.41257 | 2026-09-22 04:02:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86361c10-c73c-3ff3-85dd-8940a59c59a4 | -12.84403 | -44.34077 | 2026-09-22 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 004f4db7-86cf-3f14-82a5-eade7ade2573 | -5.78061 | -43.77231 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a38b1ff-1a2f-382f-aee5-d4eecc2f4f55 | -6.77903 | -48.66423 | 2026-09-22 04:02:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 230397df-f762-37ce-a628-5020a95a089d | -9.89738 | -48.41962 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac58499d-b613-375e-9bab-fd8a94256aa5 | -7.45229 | -44.74929 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2637ddce-cbbe-37e2-9dcd-945e61717d3b | -11.43672 | -47.33937 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 335904f3-3a7b-32a0-8819-b67ca12f7fbc | -12.56111 | -45.95536 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f656cb2-d9ba-3cf9-a332-69ee1d7ebf30 | -6.9027 | -42.95022 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 78e9df91-f46f-3dda-9b25-5363e4caea45 | -12.01935 | -47.80659 | 2026-09-22 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a6de6f10-5add-3783-8f0d-adfdacad8dbc | -7.5075 | -45.44241 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4414b25-3e95-34e0-ae6e-0d6be998d5f2 | -5.84562 | -49.78852 | 2026-09-22 04:02:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10a75435-14b0-37eb-adc0-f1d6fed98ffd | -5.78204 | -43.77262 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| caff3de7-6d0a-3689-b7aa-2935f5323b1c | -12.10265 | -45.65483 | 2026-09-22 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c88cd23-9519-34b2-b225-2ef3ea72a84f | -10.4574 | -45.10536 | 2026-09-22 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e76f352-1fcd-3037-80bf-4552ad3f7417 | -12.02327 | -47.81241 | 2026-09-22 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 535d5070-517b-30a7-b46c-a506332d5265 | -6.59087 | -39.13587 | 2026-09-22 04:02:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 38ea8eae-b39c-3c49-81f4-657732230fb0 | -7.53608 | -45.41013 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e9ca1d7-95f6-342a-8899-d5eb165434c3 | -7.35556 | -45.3484 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1673281-47c2-357f-b671-75630c7d5b52 | -12.06319 | -42.32977 | 2026-09-22 04:02:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fdf43c91-1a6c-3619-88fe-f152eb4617bf | -4.17783 | -51.24868 | 2026-09-22 04:02:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4751623e-3a08-3d63-bfad-25732d176ed3 | -7.06316 | -43.66857 | 2026-09-22 04:02:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5455dcd0-3b61-3deb-b724-dc867b4cfc57 | -10.38186 | -48.89891 | 2026-09-22 04:02:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebe27a0b-4863-3128-b201-2806293702ac | -8.11567 | -49.58768 | 2026-09-22 04:02:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13c48cef-4bb2-3ef3-a6d6-8baf6747a0f0 | -11.41194 | -46.79574 | 2026-09-22 04:02:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b99e4a5-0d23-3e20-99db-7e9cf66ebc77 | -10.05258 | -44.88862 | 2026-09-22 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34f8727d-9969-3edf-a951-9a4e8365d44c | -6.88193 | -41.69496 | 2026-09-22 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5183b491-1c27-3f24-af76-5380db972889 | -9.8057 | -48.30222 | 2026-09-22 04:02:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98028e06-78a7-3b54-96b3-4634ef8b8517 | -11.41415 | -45.37172 | 2026-09-22 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57458e0b-ec7a-3298-af72-8c1946fdcc3b | -6.9969 | -43.29573 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 93244c16-434e-3faf-a0c1-cf958c869f16 | -11.32928 | -51.37465 | 2026-09-22 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24b92f05-dc06-3f53-95aa-0a68ae785bd7 | -11.2396 | -40.25834 | 2026-09-22 04:02:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4cfb1a1d-f687-38b4-8644-dbae9bad8ef2 | -11.44712 | -47.33404 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3cfc3cab-2c13-3fde-ac2a-92c22fc02942 | -7.44942 | -44.75013 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3e8fbb4a-d40e-360a-957f-edbfd5ea64e6 | -11.42863 | -47.35457 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c347e633-99d5-30a3-bb0c-f88a434e2320 | -10.20688 | -44.15264 | 2026-09-22 04:02:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50fa21d1-8445-3653-88f1-404567e8ea7b | -8.30579 | -40.59916 | 2026-09-22 04:02:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 563d2cec-4598-3548-aaaf-600ec1d2a95c | -8.91679 | -50.93258 | 2026-09-22 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0ed63d80-aeb1-3d62-a9a8-cd2391bc2c11 | -10.84604 | -50.15775 | 2026-09-22 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4516f0e7-0ecb-381d-a47b-722d364ab638 | -10.00818 | -45.21094 | 2026-09-22 04:02:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dee539d5-cb2a-3835-ae84-383e4408c8fd | -6.97356 | -47.50224 | 2026-09-22 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 02cee714-dd3c-3a15-894c-48c787e2fd49 | -11.42461 | -47.34967 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 435d1957-4123-3964-a0c5-66c3734ee6a3 | -11.43493 | -47.34881 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca6d86ca-509f-339a-9f6d-220efa5a428e | -11.43496 | -47.3469 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08318434-0b8d-308e-a88a-16b787441bc7 | -9.62018 | -43.9369 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b811a54e-fbd4-3f3f-9b58-ff034b07f0b5 | -6.66779 | -47.37528 | 2026-09-22 04:02:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25d906ae-c903-3d28-95d2-dfe8f165e864 | -10.78362 | -50.74106 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98867509-b38d-3945-88ac-20a571361a25 | -10.45809 | -45.10149 | 2026-09-22 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09011643-b308-39f0-a390-1518fd4efcd1 | -6.95103 | -43.08749 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a2e729c-4570-3640-8c63-3f88e3a4fcb4 | -6.57374 | -44.15234 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f07431cf-0d14-3b2f-a5f8-e9d455fa81a2 | -6.58143 | -44.15761 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dc74994-4f37-3604-bf2a-71bcbd97d770 | -6.30723 | -43.79835 | 2026-09-22 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe3a5d56-784f-3fd9-b05f-c9335a9b0bc0 | -7.55326 | -42.66101 | 2026-09-22 04:02:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bad294b2-0aa6-38eb-9b58-77eca8d5c8d4 | -10.84028 | -50.15655 | 2026-09-22 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 161327a4-412b-3665-9476-4867a114047d | -11.4424 | -47.33533 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f9b424f-cda8-3367-9e7a-3885fdbf74e1 | -6.1902 | -45.32594 | 2026-09-22 04:02:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 207ff29d-3e2c-3601-a4ac-e3cb148a4105 | -11.33023 | -51.36976 | 2026-09-22 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2d8bb6e-99fd-3df8-bae8-4393646987c7 | -8.31679 | -44.75037 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 598389dc-6908-3ec5-af08-ef56114ddd57 | -12.01681 | -47.80403 | 2026-09-22 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b176104b-8eb8-3b0f-ba6c-183e3b968217 | -7.45301 | -44.74524 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 91d61359-51e5-3e48-81f7-dd6b61b52248 | -7.12871 | -48.42953 | 2026-09-22 04:02:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22349784-f157-34c0-b7b5-2153cfe3bf3d | -10.86488 | -50.89916 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 924d9f5e-1338-3be7-89d9-cefccfd23dcb | -6.58207 | -44.1538 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 149b9d97-7e8a-30a0-90ea-2ecead9beffb | -11.02254 | -48.27354 | 2026-09-22 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36fc6fc3-dccb-3770-a663-f1f2444d1927 | -11.67984 | -43.44771 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf4052ff-cb5d-3aa2-86b9-0890558375d5 | -10.46815 | -51.30021 | 2026-09-22 04:02:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1ca4e38b-79e2-38a5-861b-a4b73fc2671e | -9.56585 | -48.42958 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 581a85e1-5bbe-35ca-8d8f-61e40f0f4643 | -11.43015 | -47.34808 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fbdfc68-b8f4-34e5-8569-63dd676ec651 | -9.96919 | -50.26096 | 2026-09-22 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01fec51f-5ca5-3048-8d59-29dccb6e610d | -9.90028 | -48.49216 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92809bfe-0773-3f1f-9bb7-7c255a0905d9 | -12.14557 | -47.39881 | 2026-09-22 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 928c1df9-673d-3f65-9e50-839e9626058d | -12.09847 | -45.65399 | 2026-09-22 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a861b42f-cdb6-33e5-b897-1a6fcc53e8ba | -10.38446 | -48.89753 | 2026-09-22 04:02:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2584346d-99db-347b-9c87-573077b763f3 | -11.65395 | -43.44312 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa0786e6-8f80-36b9-be15-1d020c86347d | -11.15826 | -51.11678 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 404052ce-4342-364b-a5eb-a924410349a6 | -9.54169 | -45.39048 | 2026-09-22 04:02:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 31508af1-fb01-39ed-ad72-ce7472c03dad | -11.15731 | -51.1215 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| efab289d-9d8e-3276-a9d3-36fc9831e3a2 | -10.20992 | -44.15846 | 2026-09-22 04:02:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35b9f623-ecda-32f0-8b88-8abb694b9cbf | -11.43856 | -47.32707 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 938c32e2-63c0-3e5d-a60e-5baede5077c3 | -6.8927 | -41.69666 | 2026-09-22 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab4a1eab-8bed-3e78-987e-8651ad8035c9 | -8.82281 | -50.49259 | 2026-09-22 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 257a5211-e399-318a-890b-fa15e72bf35b | -11.33044 | -51.36295 | 2026-09-22 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18de2819-cfc7-3ce7-ac3d-d0dc5f3c5947 | -11.34294 | -43.37605 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5007ac8d-7612-312b-b151-a5740c53172e | -7.51647 | -45.44387 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f537bb34-c14f-3034-bec7-2de1d8e9556b | -6.59419 | -39.1364 | 2026-09-22 04:02:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 5415dfe2-fd0a-3144-887a-24156f7838ed | -7.51122 | -45.44757 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5dd9adb7-1c91-3207-b1fe-0f10544924c1 | -9.25466 | -41.0402 | 2026-09-22 04:02:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 93dc79a9-9a04-3d73-bc65-d8d50739cf9e | -9.52797 | -45.39261 | 2026-09-22 04:02:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README36.md)
