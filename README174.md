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

## Dados Diários - Página 174

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7648cce9-ab15-395e-962b-dc75286c314d | -10.9445 | -43.8849 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 289.1 |
| ed7ae937-2b1e-37a8-b210-298013eb9c0d | -7.3306 | -54.995 | 2026-09-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| f9925175-ec76-3a80-b9d8-c7f2edd26c54 | -7.6852 | -54.7532 | 2026-09-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 68149280-cb9e-3866-8e78-b44b13b1598a | -0.4889 | -49.1327 | 2026-09-28 18:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 8ab6fa32-c90e-31ea-9938-261b20cd0044 | -6.7369 | -55.0874 | 2026-09-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 1a5fe9b0-9e1a-31f8-8a95-a3a3369fed61 | -15.0153 | -49.5904 | 2026-09-28 18:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 2e619435-6b08-3aa7-a32e-b127b9e7a4d7 | -5.7384 | -45.0626 | 2026-09-28 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 12a13a5a-4b5a-33a7-a840-f61da08d17ae | -9.9784 | -50.1412 | 2026-09-28 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 82cdac33-f9f7-367c-83ec-8df565ce6081 | -8.1869 | -54.8025 | 2026-09-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 26eb4fa8-6816-3776-8ec7-c7205b845632 | -10.9254 | -43.8876 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 084be106-28f9-37a1-a4fb-30b46c8f0c07 | -11.8641 | -47.1004 | 2026-09-28 18:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 612f7d4d-d4f8-3697-8d84-82e87b393685 | -10.6505 | -50.7123 | 2026-09-28 18:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 003a9c7d-1978-3a20-9216-305faba43718 | -15.112 | -53.8838 | 2026-09-28 18:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 14fdc827-816c-3e99-8bf5-7dd5f7e6f886 | -11.6784 | -43.5158 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 196.5 |
| b4212058-6a6b-3260-8463-18e45962daa3 | -7.4974 | -55.0256 | 2026-09-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 243.1 |
| 863fccae-82aa-3cf3-a306-4fcfedd5c08d | -11.6994 | -43.4178 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| d7ddd049-a8d5-3735-8384-7f31c865f3cf | -9.0783 | -49.8853 | 2026-09-28 18:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 141.3 |
| f4572593-8208-315f-9735-dc1bef1716d6 | -10.8052 | -60.7257 | 2026-09-28 18:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| f3f61e50-0bc6-33fe-96fd-c50bf77d1aa8 | -10.9154 | -50.7059 | 2026-09-28 18:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 132adf7d-b675-3f55-a595-8377b58a8f42 | -11.3436 | -54.1086 | 2026-09-28 18:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 229.9 |
| 10d8ba6a-86c4-3632-86e1-7f0eb0215c28 | -10.1098 | -50.1921 | 2026-09-28 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| d6d8b1b4-ec8f-30a7-b915-6db5e5a4e6b9 | -6.3137 | -43.6178 | 2026-09-28 18:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| d5ba4377-b8f0-3ff7-83f6-20543617a034 | -10.2065 | -50.0113 | 2026-09-28 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 283b7429-805c-3a21-b966-b68b60f2f6cd | -8.2291 | -45.4602 | 2026-09-28 18:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 37bcba60-1e39-3ded-b73f-a923c2876ef1 | -10.2067 | -49.9898 | 2026-09-28 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 716ece83-4e90-36ef-9f6d-7f3f2d296101 | -10.8191 | -57.1795 | 2026-09-28 18:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 230.6 |
| 5067cf7b-d58d-3e4f-b1c3-1c31304d3142 | -12.6271 | -47.2626 | 2026-09-28 18:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 780c7c0f-15d3-3c6c-89f5-20612beb9c2b | -11.6986 | -43.4654 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| e4d7e388-eeee-3d9c-afee-ecf29ba3ba3b | -11.373 | -43.4446 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 7765f52e-e2cb-3735-a332-b6c308cdaca6 | -11.6213 | -46.7742 | 2026-09-28 18:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 3e0b3eac-e9a2-3a40-81e1-89b082fb7922 | -10.8967 | -50.6866 | 2026-09-28 18:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 96d81f1d-c7a3-3f53-8540-811b4d68294e | -10.8379 | -57.1781 | 2026-09-28 18:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 818a9b7d-e644-3fb3-b7f5-f97943702f58 | -7.6903 | -44.8761 | 2026-09-28 18:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 43a723be-3a05-3a30-93d0-1365406024d8 | -9.7684 | -44.8312 | 2026-09-28 18:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 98f05b3d-1164-3a25-932e-9a9b8accc1f6 | -8.2807 | -54.7158 | 2026-09-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 190.4 |
| 478db705-b66f-3689-aa29-161b45c7cb96 | -10.2443 | -50.0074 | 2026-09-28 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 601f0e26-1916-3659-b7c3-9d6ba1abb1a0 | -12.8061 | -54.0048 | 2026-09-28 18:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 242f4802-c28f-3f87-9b59-8b0aee78351b | -13.5007 | -61.1333 | 2026-09-28 18:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ca038552-26ed-3db9-90c4-c8fb48e250e6 | -10.2257 | -49.9879 | 2026-09-28 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 9c008ab7-6c94-3f66-92dd-45c6cabc008b | -11.3739 | -43.3972 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 74a88f6d-015d-3e2f-927a-76e9a7663382 | -10.8184 | -61.4191 | 2026-09-28 18:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 6e63d5b3-81d7-3e3d-bd01-0ed0b47cef4a | -9.6864 | -58.1258 | 2026-09-28 18:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 184.1 |
| c05893ee-cfd0-35f0-9799-f4e5816f14f1 | -13.3272 | -43.9285 | 2026-09-28 18:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 198.4 |
| aba34b43-59c6-37a4-bce9-c7b859675e2d | -12.1202 | -57.1767 | 2026-09-28 18:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 1fc974ee-af1a-3de0-a608-30f1652f378d | -10.8238 | -60.744 | 2026-09-28 18:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 202.0 |
| 238163cf-e6ec-3c23-bbdc-b52d4804b660 | -11.3927 | -43.418 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 275.5 |
| 988aee9c-5528-32fb-be18-d046d4b71328 | -10.9637 | -43.8821 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 227.6 |
| e7459ad4-7423-3eb0-a129-3cbb784716fb | -10.9449 | -43.8614 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 039d35d3-f773-3429-a686-b9dfb180fb35 | -7.5057 | -44.5733 | 2026-09-28 18:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| e56a2cb8-8049-3e97-9f6c-492efbcf6933 | -11.0034 | -54.1396 | 2026-09-28 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 5b8b9a29-ccfd-38f9-80fc-cb28a2ec6be5 | -8.6451 | -45.3489 | 2026-09-28 18:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 739ff9c6-fbee-34be-8829-9dfc49dc2fbf | -11.2758 | -43.5303 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 31c9a9c3-0c9d-3a53-b960-2a9ce1a2da71 | -5.4762 | -45.1262 | 2026-09-28 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 210.9 |
| dd1fbaae-0977-3922-8b12-5ce7268c5599 | -8.2804 | -54.7562 | 2026-09-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 2f8e9ff1-1dbb-3e5c-9978-e9bdc5eb36b5 | -11.6404 | -43.4981 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 354.0 |
| 67cfd91c-3595-3302-a6c3-bcd5a51c0fcf | -11.1966 | -44.7805 | 2026-09-28 18:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 594595a8-b494-3557-ab85-9236d8e1de75 | -7.8896 | -54.7609 | 2026-09-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| cedc360f-1741-33d1-9f91-fa8c91a69cab | -12.0019 | -57.6051 | 2026-09-28 18:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 480d803a-b28f-3909-998b-ec94d4974173 | -12.6071 | -51.9595 | 2026-09-28 18:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 16161ffe-74ac-30a0-83a1-eb1703d32052 | -10.8189 | -57.1993 | 2026-09-28 18:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 430.3 |
| 29c8efac-c796-346e-a86f-e1410455f787 | -4.7065 | -43.2003 | 2026-09-28 18:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9efc63d6-44df-33c3-ae8d-f29a2be2fbb9 | -11.678 | -43.5396 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 247.8 |
| 8782df75-b433-371a-899f-2859f818f16a | -6.314 | -43.5946 | 2026-09-28 18:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| da14446f-a57b-3065-9073-823f4d04119d | -5.4949 | -45.1249 | 2026-09-28 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| d2f4e6b9-178c-3d12-9c2d-a2e721599c2a | -10.0148 | -50.2443 | 2026-09-28 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 7884bb16-4e76-3279-83ac-54f7eb68d55c | -10.2147 | -46.706 | 2026-09-28 18:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| a41f2425-653c-3a59-afb7-6b9dddb95487 | -11.6209 | -46.7967 | 2026-09-28 18:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 5f5dfe45-c2e6-3b23-86c8-902bbf9ae63b | -10.9441 | -43.9084 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 51c8109c-1872-3b9c-a2d1-d178fa70203b | -14.0915 | -46.3096 | 2026-09-28 18:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 68fa1c31-f826-37dd-a47d-74e835ca7039 | -10.6869 | -44.4576 | 2026-09-28 18:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 4feec994-c85f-3470-a4ac-79af4185250b | -10.8185 | -61.3998 | 2026-09-28 18:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 810eb50b-3542-3886-9511-7ea9cb69a4ab | -12.6263 | -47.3075 | 2026-09-28 18:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 5b3e5883-1858-3f41-8ae7-6a2cefaf810c | -12.7417 | -47.2909 | 2026-09-28 18:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| c6d7719e-5e77-30ac-9ee4-5ba1e6bd913c | -11.3735 | -43.4209 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 5b0bc5bb-69fd-3819-9d2b-f3e8f311488a | -11.6096 | -44.1382 | 2026-09-28 18:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 245.5 |
| 807416e8-598b-3fb5-9a90-11bc8ead17df | -12.7413 | -47.3133 | 2026-09-28 18:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 5dea0475-67e6-3dfa-8bbf-e572b3f272b7 | -10.8001 | -57.2007 | 2026-09-28 18:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 177.7 |
| be80cdba-9c31-3a20-a524-7846ea778333 | -10.8371 | -61.418 | 2026-09-28 18:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 4c7ecc9d-ee69-382b-82f0-f9fbb8ca46eb | -9.9781 | -50.1626 | 2026-09-28 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 7cb8cc41-52c6-3679-a141-7e179bf199c4 | -11.1771 | -44.8064 | 2026-09-28 18:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 192.4 |
| eebed485-08f6-39d3-be3d-c3913929248b | -8.9637 | -44.1422 | 2026-09-28 18:30:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| ce5bb92a-1c2c-357a-ab83-ac4d05a40ca1 | -7.6851 | -54.7734 | 2026-09-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| f3f6de21-f8b7-31cd-8469-14ac8b668e66 | -11.7178 | -43.4623 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 388.2 |
| d85d92a7-6349-3dcd-8aa1-a82c976525f3 | -11.2753 | -43.5539 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 6eb6b394-a9d8-3abb-ba5f-6c4c47c2d9a5 | -14.3496 | -52.1264 | 2026-09-28 18:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| b84ce20b-f1d4-388e-9c38-ea4753d64cc9 | -13.6866 | -56.6131 | 2026-09-28 18:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 4a7aeded-2437-3fc4-81c5-cabc6bb027b9 | -12.588 | -51.9617 | 2026-09-28 18:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| f24cb6e9-4f53-3a64-b721-854fde382fd1 | -9.9266 | -60.7171 | 2026-09-28 18:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 287.3 |
| 6d4917d5-6a5b-36e9-8476-beb890ecb606 | -11.3922 | -43.4417 | 2026-09-28 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 685.3 |
| 6a9e8aba-5655-3770-b5d6-e5e56f8c99f5 | -6.7554 | -55.0864 | 2026-09-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 98224bdd-e22d-30fd-8900-3415119b018a | -10.8187 | -57.2192 | 2026-09-28 18:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 224.7 |
| 6d0687b5-aecd-3d04-ad77-a03d4fccf230 | -7.9082 | -54.7597 | 2026-09-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 7d3207b7-a25a-3a19-9819-7029507c5b99 | -11.1181 | -51.1091 | 2026-09-28 18:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| bef3792f-2192-3da5-b202-4ebebdeeb479 | -9.9396 | -50.2304 | 2026-09-28 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 4e2ba9df-5e27-317d-a8a1-b6b812845d9b | -6.7185 | -55.0684 | 2026-09-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 93342677-e1df-3b95-98c8-6d7c5341a1b7 | -11.3436 | -54.1086 | 2026-09-28 18:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 217.2 |
| 968c152b-cbe4-367a-814a-d127ab676b5a | -11.1771 | -44.8064 | 2026-09-28 18:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 1eb72fa6-a7b7-3cf3-a700-36f2c46513cb | -7.4185 | -55.6301 | 2026-09-28 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| c56c1cf3-ce03-37f8-b5a8-0ac321691235 | -12.3085 | -50.2904 | 2026-09-28 18:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ef2f6cfb-f2e9-3fa8-9a75-b3f1ebf60768 | -10.2257 | -49.9879 | 2026-09-28 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |


[Clique aqui para ver as próximas entradas](README175.md)
