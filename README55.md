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
| 81474664-b327-30ac-b56b-f771ece82405 | -14.75387 | -55.41949 | 2025-08-30 04:51:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87a47fd3-5111-318e-b0af-f23547ea09d9 | -13.57177 | -46.90944 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed4355bf-148a-34ff-b743-2a0e32d8d306 | -9.7818 | -64.24879 | 2025-08-30 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9df517ef-b346-31c8-85dd-901aa4448c4b | -14.32501 | -51.95074 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71ad63bf-502f-3600-9342-f2b0a8d8910f | -14.62015 | -48.07742 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7aab3379-8cba-3078-8029-f5503eb02b58 | -12.71857 | -48.20019 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a04297b5-3f70-3451-a5e6-a44cbd6ef39a | -13.75771 | -43.77228 | 2025-08-30 04:51:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 890b7fba-bbe1-3e2f-b289-02b201e1f2aa | -14.00229 | -46.33438 | 2025-08-30 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fc46b47-be87-33d8-8ffe-db6e8c537d62 | -14.00521 | -44.59062 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b03a5fdc-8d4a-35a3-bf1d-ac73d6e83eac | -13.60286 | -46.87202 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aba88b83-057e-3c6c-ac28-6cbbb05fb1b8 | -14.02593 | -44.54962 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f52be544-9601-3f4b-987a-417f714a282b | -20.08643 | -48.26824 | 2025-08-30 04:51:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9df58409-8e45-30f5-acf1-2e4af8c2ac9e | -12.92174 | -56.97794 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a8c7e085-5be8-341e-bfa2-7835a1c224b6 | -13.37055 | -47.00841 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0bdcacbb-3337-39ce-b7a5-561bd26dff8f | -14.01015 | -44.5913 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e86a0a9-1405-3da0-b064-c9eaa7a862e6 | -11.30533 | -63.30195 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fad8738-0215-37c1-b60b-b4ac3e443ccc | -13.41185 | -46.95373 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44cff174-bf7b-3f23-b169-be64e26fb74f | -13.50739 | -46.94312 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41b1c82e-d0e1-3ffc-a293-f86f8d415bf5 | -13.51654 | -46.84185 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36ff7b65-dbf2-39c2-a124-9ce841bf6c07 | -14.34409 | -53.27052 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00b1baa1-9ef2-3a2f-b8e5-bc70fd534284 | -13.43551 | -57.181 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31feb3e2-20ac-3e48-90db-720c362d7ab3 | -15.21993 | -53.8018 | 2025-08-30 04:51:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41bf6d6d-836e-30bf-9818-24a13e5bf8ba | -12.92442 | -46.35855 | 2025-08-30 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28462ece-02b3-344b-9f4a-9dbd6011132a | -14.00098 | -44.5844 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c1d02a7-b74d-329e-831d-2f1960c6396f | -14.02087 | -44.54719 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 69af3f02-1ad0-36fc-b03d-92b2053c971b | -14.60589 | -54.50074 | 2025-08-30 04:51:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4397fb4-449e-3380-9c5b-2b3286321c2d | -13.97738 | -46.3241 | 2025-08-30 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ac56c5e-744c-3f40-b5d7-134b15bdb5d3 | -13.36892 | -47.00916 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa6a0831-2f32-38aa-bf69-08108e6dd1df | -12.83548 | -48.1363 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1518812f-92a5-3adb-aa64-30342bd9861d | -14.34733 | -51.89513 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 085f450a-fd22-3cdb-9afa-767573254689 | -14.0045 | -44.59617 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fbca4cfb-08fd-3018-853e-314194540bd8 | -15.30972 | -46.09549 | 2025-08-30 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4147551-ca18-3da3-ba08-26eaced53825 | -14.02866 | -44.48545 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de09146f-ea47-33e6-af17-b57cc19c5d0d | -14.3516 | -53.33066 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c597881e-c100-3e3c-9611-f73fffc33488 | -13.37214 | -51.75462 | 2025-08-30 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c4dd692-0bf9-3612-8a99-6c0e8c3ac91f | -14.34561 | -53.30386 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee4bbfc7-b445-3aae-aeec-7af619e5bd02 | -14.38932 | -53.223 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 641d554a-2b76-3d9b-b4fb-fb28a620dbf1 | -12.92564 | -56.97865 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8722a099-96f1-31f7-bfdf-de0aef9d01c6 | -13.67507 | -46.87793 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ef8edc11-2c6a-32cc-a6ba-35ed074ccecd | -14.84522 | -46.74275 | 2025-08-30 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b016fe29-0d85-356f-b3ac-a559bd6b02ed | -13.37987 | -47.00214 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cfb46b56-b93b-3a50-ae22-f90bda637374 | -14.02332 | -44.48879 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c4f394e-16d2-3b5c-9d0e-ed7f0afd5902 | -13.35153 | -51.77707 | 2025-08-30 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49d30ba7-2f32-3e17-8489-c8c8afdadc1d | -13.55334 | -46.95048 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19b1ae0c-41fc-3636-81f5-185dda73a581 | -14.59287 | -54.49463 | 2025-08-30 04:51:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f1e2a09-3496-3719-8677-5dbe9f51fb9a | -14.00202 | -44.5808 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52e0028c-b514-3ffa-83b1-487a5943459b | -13.40241 | -46.96062 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14a2005a-1aaf-3b0e-b73a-7838eacc4232 | -12.93932 | -48.13308 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cefab26-d629-3326-842a-dc720b56b6b7 | -12.63469 | -57.01298 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc25eda1-0034-31d8-bc4c-3a060176240e | -13.39889 | -46.95503 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a80b17c5-30c2-363b-a367-fe0a235cb2c3 | -13.39655 | -47.00434 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39606f8b-5562-3677-93af-5094d26f419b | -14.35217 | -53.32707 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f00ffbe0-2488-3f72-a427-61f48cd57feb | -15.03117 | -57.18993 | 2025-08-30 04:51:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1505a776-ce9a-3083-a2e9-5e42edfda756 | -12.93045 | -48.11212 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37744f2e-f929-38a4-95a8-6931f5f1466e | -13.65235 | -46.91898 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 748e2ce8-6cf6-3773-ac28-d3c99f32cd19 | -13.17064 | -50.5865 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ee95e8e-0915-3042-b251-0a59aa19ace9 | -11.35221 | -63.25484 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea932388-88d7-3365-a0b2-6ff7e7eb9ae1 | -18.92938 | -47.0683 | 2025-08-30 04:51:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf73dcc7-5bb4-36c6-b85f-14445108909c | -13.38342 | -46.9754 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 725a4ca9-a732-36b2-a351-b948f28f058f | -13.80099 | -52.75262 | 2025-08-30 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4227c2e4-b0e4-3f58-889e-05802e1dcc76 | -11.3582 | -63.25615 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d20c27d5-bd64-3d90-b7ac-4afeeaf9df30 | -13.49133 | -46.84116 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 394c7f58-c7f1-3014-a139-901928358975 | -12.51479 | -53.82532 | 2025-08-30 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed0d1d12-0142-3c20-b588-487bdf65e4f1 | -13.50035 | -46.83805 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea09045a-d1e7-3433-952e-5adc5dd3e481 | -12.62293 | -57.01081 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c514217-50df-3cf1-99e8-6437fe8fe1da | -14.3758 | -47.85143 | 2025-08-30 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55c079a8-0102-361f-a056-a2f0cbd37f34 | -13.19435 | -45.27615 | 2025-08-30 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd9a2132-eb6f-3404-9376-5af6e911560c | -13.36528 | -47.00481 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 721e09d9-21c7-3615-adf0-ac9a48ba31c5 | -16.04667 | -49.03959 | 2025-08-30 04:51:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d6d805e-2aff-36ae-9009-be06e716eb4a | -12.82267 | -48.11567 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59c634d4-dc37-34a6-91a6-956818b2caae | -13.48712 | -46.84055 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f695a15e-dd6c-31a3-aa95-65d8cde97222 | -13.35208 | -51.77348 | 2025-08-30 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b8d2efa-231a-352a-8051-8b5c52a2d889 | -14.49134 | -52.05163 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dafd78e-f6c5-38a1-a6a8-84320f066f74 | -12.69394 | -48.15279 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52144492-52e4-300c-b258-5343f88f6a6b | -14.46014 | -52.02116 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9bda654-ccc9-3c12-8d68-db236a5e4eb1 | -13.42006 | -51.82125 | 2025-08-30 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99599d24-1117-3bbd-9c9b-c8f5b90b2d7c | -12.93431 | -48.11266 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48c5e9b4-5975-3afe-b083-27a1b8849b6e | -12.94842 | -48.12437 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae6c8555-9e56-3d7a-8fbe-2390e87762be | -15.20559 | -56.06081 | 2025-08-30 04:51:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6f1a7dc-6e0c-38ae-8460-0a69d1d16742 | -15.10418 | -48.16724 | 2025-08-30 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4a40164-95ca-38fb-bffb-c022f3a6b9c6 | -14.62406 | -48.07832 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c9a47231-ee89-3714-bbca-46a547eafcfe | -16.58432 | -54.6503 | 2025-08-30 04:51:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc44d3c5-fcab-361e-87ba-0d59ba6c2813 | -13.56496 | -46.92796 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5fd7691-cd62-3f9c-980f-f56bb6cd1fd2 | -13.40546 | -47.03271 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c50dde6-2474-32a1-8b78-111d55a9fa7a | -13.37364 | -46.97527 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24c3fab1-86bf-3d09-9073-0dcc8690b754 | -13.35865 | -46.86767 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f0d004c-8030-3303-9587-de75ec63e2e1 | -15.21499 | -53.78979 | 2025-08-30 04:51:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ba18851-6380-3191-8017-46070b73ca4a | -13.40597 | -47.0289 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f490dfa-b2eb-388f-959f-f436eb9dfdda | -14.01961 | -44.56014 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 94d61814-6497-328f-8fab-75055d83f8de | -12.82982 | -48.09277 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2f8f52c-8faf-3e4e-bc7e-86b30e2c51ce | -17.45282 | -44.48952 | 2025-08-30 04:51:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f91d9d47-f95d-30d5-80c3-f0eb20b3a375 | -13.37938 | -47.00575 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e29cfb9a-383d-3a5e-9710-acf5a4cfbd18 | -13.37096 | -46.99453 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eef7c9ee-af1b-3924-8fe4-67bc735b599d | -12.92974 | -48.11717 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dbd1099-fea9-3b07-8cba-60faed039261 | -13.37152 | -47.00105 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b055c042-b8de-33f3-9697-c66fc0c0c5b6 | -12.82103 | -48.18305 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50e7aff3-5901-3b17-9167-3eba815ce89c | -13.36421 | -46.99212 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6abbd7cd-0c5e-380d-aabf-f3e154ecc71c | -12.42552 | -63.92095 | 2025-08-30 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c298eb9b-f2b5-3828-aaf3-f27318838349 | -14.32096 | -53.09414 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cf30c15-bdf6-3cf5-9b2b-88799af19794 | -12.42744 | -63.91139 | 2025-08-30 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README56.md)
