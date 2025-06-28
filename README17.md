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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70398153-fd22-3a33-9e35-610ba606b793 | -14.53899 | -53.83699 | 2025-06-28 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6308f99-5fa0-323d-9c94-08487cb7d03c | -11.05084 | -55.07767 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 01f5ca97-6c58-359c-ba0c-cf738df81921 | -14.53806 | -53.83654 | 2025-06-28 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39183d86-8d03-30af-839d-8d996ee3830d | -10.95504 | -49.25298 | 2025-06-28 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae512827-a047-3c43-8e13-f0f5ae6d4bf6 | -11.05513 | -55.37653 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7baf6f76-e92d-3849-9981-8511a4ca1a78 | -13.66824 | -43.66885 | 2025-06-28 04:29:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf1405a0-f089-3ff4-9901-23fc49af9b2a | -10.8213 | -53.74552 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e650106-8873-3e57-86bf-c53d84ceb64b | -13.23623 | -49.83522 | 2025-06-28 04:29:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71084ce3-7701-367a-bea1-f73d0897abbd | -10.82431 | -54.0481 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a33936e-7478-3094-9bd8-dc75b2b95b8d | -9.72328 | -56.18684 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ac3b335b-f576-30c4-9dff-2902b6d860a8 | -10.82855 | -53.75593 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6207602-af65-3e2c-8567-981c149d13d8 | -9.71333 | -56.18144 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 30d61fb7-c295-3d27-94b5-b42bf48e25f6 | -10.83296 | -53.75677 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4ad47a2-5d72-3c34-a94a-c5dcbc06ded8 | -16.13166 | -47.49044 | 2025-06-28 04:29:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f67245a-b56f-342d-81bb-69a7180baf32 | -15.26389 | -51.47108 | 2025-06-28 04:29:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7be19b10-4804-3c4c-bbd3-8ee97db31108 | -14.53388 | -53.83584 | 2025-06-28 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20a55bb9-62fa-35d2-ad8f-177ec71debee | -9.7068 | -56.18707 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 748f05a5-6dbd-3f2c-8c7c-1b0be0453263 | -10.03753 | -54.33769 | 2025-06-28 04:29:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 163d6ac5-3e7a-3b0d-b2ca-23f6a911866b | -10.84177 | -53.75842 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 260a7467-ce57-3630-8030-728f788a9424 | -11.2678 | -52.74852 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 518b457c-6045-3a57-9a07-e062caeb6490 | -10.8257 | -53.7464 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b51fb97-7751-3213-82c2-0872aff93d77 | -12.25667 | -46.75926 | 2025-06-28 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 254e35a3-7632-32db-92f3-eb7b79e7df56 | -11.88365 | -58.73481 | 2025-06-28 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd7cd193-994b-30c9-acab-d82781a7a896 | -11.56955 | -47.62502 | 2025-06-28 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e893a8c7-0a47-3e67-ac3d-12a64d8e0602 | -13.66894 | -43.66398 | 2025-06-28 04:29:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eb5e1ef-2944-3271-81d7-648af57708bc | -11.03942 | -55.37919 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| c9db263b-3886-3788-90f9-4d429f922658 | -12.25755 | -46.76649 | 2025-06-28 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b6286444-69d1-348a-9480-a2b8a907600b | -9.70742 | -56.18376 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c7e676dc-6b25-3bd5-bb21-af04c5d6ee94 | -16.45171 | -49.51613 | 2025-06-28 04:29:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2443a79b-18c6-3b52-90ad-c70be7c515d4 | -16.35917 | -49.33206 | 2025-06-28 04:29:00 | NPP-375D | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68bbb472-ab4e-33d5-9a4b-d4ea8975c784 | -10.83737 | -53.7576 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 87010f94-f8a3-3270-9969-f9d5660065b4 | -12.02243 | -47.77427 | 2025-06-28 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29695579-7572-37e1-bafe-ad8cbaa0f021 | -10.81195 | -57.76204 | 2025-06-28 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35c44472-22d6-321e-8e97-d1d94e0f4868 | -11.87853 | -58.72918 | 2025-06-28 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17665a6c-de26-3de1-a00b-0c7d2e1c1d66 | -11.4434 | -54.46701 | 2025-06-28 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90dbfccc-13d2-3724-a117-719386c4630a | -11.04434 | -55.38002 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| f2afb396-3618-3008-a0f5-f79f9c02139a | -12.25979 | -46.77419 | 2025-06-28 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 180d0c90-b469-3cde-9996-7ae0ef6e6941 | -11.84242 | -43.79845 | 2025-06-28 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5dd2f358-6c11-3f22-aadc-944ea11e3cd9 | -14.8911 | -48.39837 | 2025-06-28 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 922b4058-8524-3b6f-8f1c-74cd70d5bcef | -15.56737 | -47.85652 | 2025-06-28 04:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c3d4a45-a400-33e3-8f63-3bbf3f8f823b | -11.58096 | -52.12047 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 34ee628b-bbe0-3bf1-8d9b-d71f379ed629 | -16.54731 | -47.78874 | 2025-06-28 04:29:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e84c517b-3197-3bfb-b46d-5bdafafdedb8 | -10.82777 | -53.7603 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83fb9ded-708d-38dc-95a3-453bead6e02e | -13.65122 | -46.81255 | 2025-06-28 04:29:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26085698-4123-3609-870d-a3c634dd15ac | -11.66576 | -46.72849 | 2025-06-28 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a13313cc-b1d5-3706-8baa-26c30e4d4515 | -12.26089 | -46.76703 | 2025-06-28 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 17b1107a-25c5-3c7a-80c6-bf61c314ef0c | -13.29241 | -57.09418 | 2025-06-28 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21c46047-65a6-3887-880b-b0a42e18fd87 | -11.04045 | -55.37369 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| aab9263b-0a05-321a-bf49-dbd58bfee7ae | -11.8065 | -56.9631 | 2025-06-28 04:29:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed6f895b-cb62-3b79-9c09-aa4a7b14d1fe | -10.03379 | -54.33186 | 2025-06-28 04:29:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0b572aa-720a-3367-9238-071902f80bac | -11.66187 | -46.73152 | 2025-06-28 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 595973d1-b7f7-3f97-a064-57b10c4b722b | -12.10873 | -54.58461 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62589b29-8d07-3c45-8863-9c561eb9adfc | -11.57791 | -52.1147 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 81cb1330-98ae-3e2b-ab69-2c6ebc113750 | -12.26145 | -46.76345 | 2025-06-28 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5d4d9e34-63e9-3e8d-aa26-4dd841313ded | -13.13783 | -56.80864 | 2025-06-28 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6e1f879-b247-3024-b578-c740180857ec | -11.5658 | -54.51785 | 2025-06-28 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43e3d3c7-4704-3097-b625-3f275e08e4fb | -11.04923 | -55.38099 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| e584ff79-d83a-324e-b60e-a409ebff8531 | -14.83104 | -59.79966 | 2025-06-28 04:29:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cbe94949-fc4c-304b-885d-6d26a3ac5924 | -17.13823 | -46.59501 | 2025-06-28 04:29:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1f320f2-26a3-3801-8ccb-ecb7b33b75fb | -12.11242 | -54.59025 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da594aa4-51ef-3785-b8d5-1535e1995d90 | -12.10783 | -54.66821 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d43b673d-e1da-3638-a874-1f77bcf39cce | -13.64786 | -46.81201 | 2025-06-28 04:29:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86b4f126-81c3-3eb4-981a-31469674f6b9 | -12.2581 | -46.76291 | 2025-06-28 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 45028779-e5df-3c39-9e19-b736debd8c45 | -12.262 | -46.75986 | 2025-06-28 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4b713f0d-8968-3779-ad32-60cdab2e174a | -10.29812 | -57.14032 | 2025-06-28 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 660408e4-f785-3d19-960e-9c508d9da6db | -10.95986 | -48.15285 | 2025-06-28 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9d5fb6e1-09c4-37c0-8f19-7009b062eefd | -11.92029 | -54.81414 | 2025-06-28 04:29:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66ad16ec-e748-39b3-bcdf-7d532d220233 | -11.05127 | -55.37006 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2c43d574-88fa-3dc7-8566-4a6b12dfe815 | -9.70087 | -56.1895 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5340f898-53ff-3373-8a52-12a1353bcc37 | -11.05109 | -55.08151 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d429d19-8a00-343a-aefe-b3e49043f6c2 | -15.26029 | -51.47042 | 2025-06-28 04:29:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f8960cd-e654-3089-946f-9aae4f5a2b13 | -11.26514 | -52.74847 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 24f0d797-2368-3f39-a867-9170a88112a3 | -11.83084 | -47.53014 | 2025-06-28 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a04325b7-f8b5-3c18-a915-478b6bf77ebd | -10.16341 | -53.92601 | 2025-06-28 04:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fd49c23-7d9a-37b4-9fb8-29ad28f8514c | -11.83417 | -47.53068 | 2025-06-28 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b61a75b-007f-3c8b-aa35-aab20907a362 | -13.2985 | -47.5141 | 2025-06-28 04:29:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5862d458-bdc8-3639-8333-93db55457af5 | -14.69549 | -53.39722 | 2025-06-28 04:29:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a3fd4bb-53ca-322c-a679-17cb3fbc5d90 | -11.26646 | -52.75597 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b71fbd85-b39a-3337-b32a-400fa749bcb9 | -10.28394 | -57.00933 | 2025-06-28 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4ebdeea-a358-33f9-aac6-73909ca52604 | -10.841 | -53.76276 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c4945a28-0f1c-3af4-a25b-1c558351364f | -12.50604 | -58.35507 | 2025-06-28 04:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02da2521-4513-3208-8cd4-4f5d7b72bd16 | -12.65951 | -54.10149 | 2025-06-28 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd7fa323-20ea-32b8-b642-683465a33545 | -11.26796 | -52.75671 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7a0aa768-b867-3aa8-ac7e-116fc4de3cfb | -11.04639 | -55.36905 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 182e4e90-0802-395c-a0b8-d40801ad5288 | -9.72267 | -56.19012 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ba671017-8398-3f05-ab35-67ada840115f | -11.27664 | -52.74638 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3a27046-e7dd-34d0-834d-3857b2b8a1cf | -9.7015 | -56.18616 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03c7ea23-8966-3850-b33c-8bd622757390 | -16.21788 | -46.00683 | 2025-06-28 04:29:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6a79926-f5ff-30df-875c-5243df31faa2 | -12.03591 | -48.75275 | 2025-06-28 04:29:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71a04fb4-c0ba-3435-8696-551bcecba1b6 | -11.77201 | -54.36722 | 2025-06-28 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6815742-def9-377b-9727-bc665d1b7890 | -12.65711 | -49.46766 | 2025-06-28 04:29:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f4e62c2-90df-3c10-a158-dbf0eb189865 | -12.2023 | -49.64085 | 2025-06-28 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15a12858-f086-3cd4-85ad-cbd236ebf5b6 | -10.83218 | -53.76113 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1343abdb-cad8-3ba6-94be-ebb4f999b07f | -15.35579 | -49.05015 | 2025-06-28 04:29:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d67c8e5-a84d-34cc-bbee-8663187bbf51 | -11.83361 | -47.5342 | 2025-06-28 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a25dc3c-430e-3ec9-bfd8-ad20444d1ebc | -13.29795 | -47.51764 | 2025-06-28 04:29:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4568ce9-0d3f-3bea-8d21-8cfaff740c6c | -14.53481 | -53.8363 | 2025-06-28 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66a932e9-45a8-333f-afa6-7cac37931146 | -10.83009 | -53.74727 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1278c1b9-38b4-39d4-b688-2202c6b18c4b | -11.18911 | -55.92767 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a982212b-1b35-34e7-accb-d1a2c633a7a4 | -10.5029 | -53.58506 | 2025-06-28 04:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README18.md)
