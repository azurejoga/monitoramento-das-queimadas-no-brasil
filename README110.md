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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcbe4842-75a1-3458-8acf-65d04183cacf | -4.85575 | -42.20179 | 2026-10-05 17:15:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| bea2f89c-b02c-3da6-97b4-2426c5ba6b29 | -3.84464 | -50.31165 | 2026-10-05 17:15:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| eaa17353-25b3-34fb-9881-657a783f5ac4 | -4.0611 | -54.05315 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 9cecacb0-72a3-3fc3-b26e-a98ceebd3d46 | -3.66857 | -55.94635 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 038dc32e-f391-3fa2-b768-c6559c335a88 | -5.18776 | -42.81363 | 2026-10-05 17:15:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ae5b17e7-8931-3433-be57-ceaee1713e43 | -4.21005 | -53.45884 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 31196c45-bf20-3e8b-b80b-2efb771d8c54 | -3.10449 | -53.70488 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 790bd626-06e9-39c6-93d6-0a702aeab9db | -6.20354 | -44.80304 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7a222ac8-2cd8-3f8a-a95d-c7aa04153e43 | -4.05845 | -54.03588 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 86c34843-7e8b-3230-9e25-1c0d2e27d2cf | -8.52888 | -54.602 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 63f261e4-cd57-31ce-81aa-ca2f79021630 | -5.26087 | -47.92652 | 2026-10-05 17:15:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9d092087-de25-39a3-9aa1-2ecb072e44f2 | -3.11449 | -53.70337 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 1090b2c6-aac1-3319-af22-67efd9c3c16f | -6.70945 | -45.23006 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 02965f76-f213-3642-a11a-895cd70a8127 | -7.82368 | -45.32372 | 2026-10-05 17:15:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| da93306d-d399-34ce-a8ac-2f96fcb97ab5 | -6.1596 | -53.91575 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2be6c12f-ed47-3cb9-984b-0e7157b477d5 | -3.05831 | -54.21567 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| fa8eb968-1f72-3c0c-a1f2-61f0f4fe2638 | -8.52943 | -54.60563 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd5f3539-7e5a-30a5-bf8b-8c4d72ae1285 | -3.66014 | -55.50095 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5799ba57-2b42-34fe-96a6-e383655ef933 | -3.28931 | -42.26195 | 2026-10-05 17:15:00 | NPP-375 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 304f85e3-fa98-32b6-908c-12691a1fddc2 | -9.45223 | -48.89697 | 2026-10-05 17:15:00 | NPP-375 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a218497f-2a39-36cf-a3be-ca92853b72f7 | -6.20818 | -44.79879 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 20392d9c-75f3-32e6-b61e-263d0e8cc195 | -4.95635 | -40.56203 | 2026-10-05 17:15:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 8dab95c0-ba3f-3231-8d69-11cd04cdda7b | -10.8777 | -61.40669 | 2026-10-05 17:15:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cb8bbde1-83d1-3741-9a9d-02622f994df5 | -8.52761 | -54.58758 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 94693540-f2b1-39ed-b6a4-11e586fff8de | -3.10474 | -41.83238 | 2026-10-05 17:15:00 | NPP-375 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 7f836fb7-9da7-3eb9-9ccd-9b2ffea5215c | -4.06283 | -54.04228 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| b0ad2837-95e1-3462-b4c5-8eac45d7ca46 | -6.91821 | -59.26346 | 2026-10-05 17:15:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c8678e65-ed84-36c5-840e-52a368fab690 | -5.12569 | -48.105 | 2026-10-05 17:15:00 | NPP-375 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 1749493d-ca8c-352d-8aab-431b25d241d8 | -5.55699 | -44.08393 | 2026-10-05 17:15:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c1b39406-cfb8-35ae-9db8-10e0629bd9e0 | -6.07365 | -53.83736 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 970b6d2a-1ee8-3daa-89b3-6ca79b01e688 | -3.82453 | -55.61439 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8a428f59-5d83-301d-9627-bbfca9e1f1f2 | -9.38208 | -49.61533 | 2026-10-05 17:15:00 | NPP-375 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6099913d-e3e2-3fec-986d-404cc07e948c | -3.22643 | -53.87811 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0fe4a23a-64e0-3469-a112-4d9609ba616c | -7.65003 | -44.37621 | 2026-10-05 17:15:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a17cfcac-3578-36b5-9aa8-11ee38aa7dec | -8.51891 | -47.43837 | 2026-10-05 17:15:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f6259537-d38f-3a34-9434-c898ff1974d0 | -6.07033 | -53.83787 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 65ee4f0d-3b46-3f2f-9186-d580a2151a8a | -8.66258 | -54.53707 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| b2992b7f-1f88-3cdf-9606-0561cd05ea82 | -3.07271 | -54.15631 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 8a3842db-7ed7-3ac5-9b48-4ac4d2a33451 | -8.66704 | -54.54382 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| eec181a8-d5fc-3dbc-85f2-07203f181d2c | -6.42417 | -43.46405 | 2026-10-05 17:15:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 9b5d2c57-5a17-3b48-86c8-e622ea709939 | -8.62589 | -67.00611 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 475fb386-9694-300b-b98d-e2fc254bb706 | -5.26517 | -47.92583 | 2026-10-05 17:15:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1c045fa1-91ed-306b-a5cf-8dc881dcea1e | -3.2859 | -54.17944 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 2ecc1de0-15ba-3a0e-a325-0fd5c819f766 | -3.57136 | -54.65373 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 06894dc2-5ebc-3077-85f9-bb8debca1ae8 | -3.28536 | -53.84372 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 52141182-4265-3a43-b133-d68f20d881c6 | -2.46325 | -49.39182 | 2026-10-05 17:15:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a1486fef-a0a8-3952-8dcc-820bf2aa11ee | -9.1105 | -64.37905 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 67aff466-36e6-3612-b875-fc0d2c85b58a | -7.22415 | -55.20129 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9f9c4d6d-f491-3ddf-8ea1-c40376f91511 | -8.86246 | -66.79758 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| e13ce176-ec4c-338c-81f4-ca8be22c8fa0 | -3.06554 | -54.15387 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| f186e2e5-1d15-33a7-8cf8-9aa001c67bb2 | -4.80056 | -42.14779 | 2026-10-05 17:15:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 210b23d6-a832-39c4-99ed-77d073fefae1 | -4.853 | -44.5174 | 2026-10-05 17:15:00 | NPP-375 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| bb33c27d-a049-3e53-9f6b-a0a7f504baaf | -4.61006 | -52.58775 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ab56e5d-803f-3391-b007-1b6f827733a3 | -7.55654 | -46.72859 | 2026-10-05 17:15:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 06080115-a6f6-33c2-864b-5ba2ef774d8b | -3.09944 | -53.71633 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| ba742005-39a0-361c-9bbe-c19ca204b45b | -3.46368 | -50.09967 | 2026-10-05 17:15:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c927e1f7-8cee-3bae-ba31-bc520a081c55 | -2.62777 | -49.30585 | 2026-10-05 17:15:00 | NPP-375 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a1882fac-95a4-3db1-a999-31cb77e601ae | -8.62738 | -67.00428 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 44cbb360-dc2f-3774-b532-41ec909efaf5 | -2.57525 | -49.15025 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3eeaefb9-4a0b-3ed9-9410-760fa901dfa1 | -4.0534 | -54.04725 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 120a0b27-fdd1-38e3-84a9-bea3932c3744 | -3.28918 | -42.25892 | 2026-10-05 17:15:00 | NPP-375 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 02f40ff6-0bd8-3ba1-8c07-ca3832849cec | -6.90827 | -43.67595 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62683245-6baf-33ff-8eb9-94bbd89f9a25 | -4.26159 | -59.2102 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| ed273cec-4047-399f-9025-33591c79206b | -3.28483 | -53.84026 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8705d64c-cdd3-341d-8599-ec0e7eb99388 | -3.60036 | -54.04802 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 379b87ff-54be-3134-a0ae-0be6a68023ba | -4.17828 | -55.69365 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d6684b82-8501-3344-819d-1e5b42dade0a | -4.80147 | -42.1529 | 2026-10-05 17:15:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 59cd4f5d-ea70-3b0b-b563-252ce4a1ec40 | -5.10137 | -42.86081 | 2026-10-05 17:15:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9dd434ba-3d23-3715-82c6-6d5db8b27140 | -6.42485 | -43.46788 | 2026-10-05 17:15:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 45810f76-2db3-3494-a440-cd286cf006f2 | -10.30797 | -63.39794 | 2026-10-05 17:15:00 | NPP-375 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 46d63a84-63ce-3f49-9c0e-b73eab3de966 | -5.62551 | -41.28949 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| b4d4edbd-3b2b-3de5-add6-dd90ce7614f4 | -9.91767 | -65.01825 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.4 |
| f9245b6b-e1bf-36e0-9cb6-bd3904a7ba4c | -3.23124 | -54.37538 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2f99164-ee97-3339-9fc3-f816bea9cd90 | -5.98318 | -40.91309 | 2026-10-05 17:15:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| a5560ff5-7ced-372c-80ad-8200bf502ecc | -3.5716 | -55.41623 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2c0f8fbc-15da-30b0-8f26-cf5107134616 | -2.32954 | -48.38698 | 2026-10-05 17:15:00 | NPP-375 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 6748c84d-143e-3208-9cfd-aed87600ed10 | -4.05951 | -54.04279 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 1ae13131-9dac-37d9-aa04-70f36c1b461a | -3.64893 | -54.05473 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 40b08790-e2ad-3f1c-a5a6-bbe5c20d0e3d | -3.23155 | -54.333 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03108652-82f5-36b4-9420-2a2ceec116f5 | -6.82436 | -58.58769 | 2026-10-05 17:15:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4317bc2-c167-3027-9727-ad9dce339032 | -4.39258 | -59.55597 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 7ee0121c-04e4-3354-b547-9c073ca83545 | -5.26681 | -47.90891 | 2026-10-05 17:15:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| ba42aee5-fb9f-3bf8-8919-9f07b6d15352 | -3.66803 | -55.94269 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 69a10a79-cf03-3c24-9c92-0f3d6ae307c6 | -3.27951 | -54.26928 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18b89b7c-af79-31fd-88ab-0ce9a6a02868 | -4.18177 | -59.40396 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d35ef433-4361-3afa-bcb1-f05a39defdba | -9.5201 | -46.81931 | 2026-10-05 17:15:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f619f5d1-8d7b-31f4-a7ec-e92da5d582e1 | -3.00542 | -53.87012 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3cb58d61-1c78-372b-b584-35223857d5d8 | -7.49726 | -44.42296 | 2026-10-05 17:15:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3c9d56e-46cc-32b1-baab-815eb2c50cde | -10.95764 | -60.90227 | 2026-10-05 17:15:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 99afd3bf-242c-3d82-8a8b-0d156af26093 | -8.55992 | -67.06454 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 7eed842a-9ee3-3473-a42e-786670f75ad5 | -8.53708 | -54.60474 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 95ec7323-f33a-37f5-b60d-92880015ab62 | -9.40305 | -65.89442 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0e65d5f0-e86c-3966-a701-ac3c52969ab6 | -6.8461 | -41.79957 | 2026-10-05 17:15:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| fe8bd5de-8914-35e4-966e-200b92e765e1 | -8.53315 | -54.60162 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 26583bcb-6632-328c-86a4-9de67687eaab | -4.12982 | -54.2582 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ab2bfe1-fb81-3b61-be3e-9128811f9779 | -3.46441 | -54.59634 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| a12dd034-8040-3377-9133-58794d8bcbf4 | -9.31669 | -49.64726 | 2026-10-05 17:15:00 | NPP-375 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b0bafc6f-ca88-3644-9033-d20aa04cc01c | -6.607 | -41.55574 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f6e77127-9be5-3c76-b29c-a97ee7ffb3da | -3.0888 | -53.72897 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ff059fc9-e43d-3d65-938e-38999562c226 | -3.82099 | -41.79604 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |


[Clique aqui para ver as próximas entradas](README111.md)
