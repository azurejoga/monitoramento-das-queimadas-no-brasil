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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cebc67a-7067-301a-8936-c8578fad3f2b | -7.46254 | -45.49669 | 2026-09-23 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11bf544f-17bc-3195-b104-bd0650938f74 | -7.43463 | -49.83926 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4b904ada-21f5-3dc3-b1d4-a3277b4335a9 | -5.91254 | -51.95698 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e0c5e87-838b-3905-b716-409915e75094 | -6.75227 | -59.05661 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4467c6ea-8811-3629-9183-624566a6101c | -4.16526 | -60.76796 | 2026-09-23 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29eb78f7-6095-3469-9148-1d93c42b9829 | -4.27722 | -55.43033 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcc35a68-cdcd-31ef-840a-1aac0e955b3f | -4.00727 | -52.09391 | 2026-09-23 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59701041-14d1-3ed4-a4ef-722459d11f56 | -3.83292 | -59.38498 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d7ff3e9-4d40-3a2d-8669-2ccaa346ec7b | -5.89215 | -52.04317 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2de7d736-1819-3112-8975-821e182128c1 | -11.40317 | -44.02781 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 40ea6c62-3754-3efc-9ad0-dc06b97c70bc | -6.81806 | -47.87352 | 2026-09-23 05:04:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 521f27fb-2477-3d34-a266-44dee93b5697 | -6.72544 | -44.14861 | 2026-09-23 05:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b48f4ae4-faec-380b-b34f-18debd84f9e4 | -10.29068 | -50.49333 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc03fc7b-6bb7-3029-a0f7-a0678a0ea9cf | -5.41178 | -49.18808 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98bdcfa3-81bd-3a74-93d1-96c4c0681266 | -5.31345 | -49.05384 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3cc6497-fc29-3236-b2a2-e91c32570b92 | -6.169 | -52.05065 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b8c10f6-9e4b-3229-842d-241fa44ccd8b | -4.38448 | -60.96309 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ce695b6-52a6-3ad2-823b-af37f5cbeb62 | -11.29201 | -51.37117 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ff978867-da51-3fcc-9664-5ddc7972f276 | -6.13163 | -57.7596 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d79d63d4-e8ff-30c5-ab4a-22197cf5531f | -7.401 | -55.21894 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f0cb396-4349-312a-886b-a49403bd75e5 | -3.85784 | -58.82179 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9cd8cddd-d4a3-31e7-8648-29b51e587906 | -6.62695 | -59.99181 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d7958dc5-690b-3cef-9359-f924168bdb58 | -8.3112 | -54.77382 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 03c52e2d-eaa7-361a-8b17-bdb454960062 | -8.14907 | -54.80093 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa6a5461-cee9-38ba-8cd3-62f8bd9d2746 | -6.22148 | -53.04261 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b25af43b-37b9-3699-a607-f65c7e559ab7 | -6.46557 | -51.52084 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5b615d4-0191-361a-991e-6cdd067bfc9a | -10.54281 | -43.98425 | 2026-09-23 05:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bfb4111-8630-3aa2-ae76-c823b7adb184 | -4.26112 | -55.76081 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c01f658-d7d3-37a3-8421-d3557898f998 | -8.80157 | -44.28324 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7401c5a-8b4a-3130-9546-2e0d7bfa57aa | -9.14933 | -61.19014 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e36bf81-c354-3ddd-a301-f1c45b2bf4e2 | -4.13357 | -54.25241 | 2026-09-23 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26f1be15-de48-3e9a-b6b5-c7bb6dd2b446 | -6.61731 | -43.73539 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b9bbbbf9-3755-3a01-9c8e-c9e4aae56e80 | -5.61505 | -45.25008 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cca8fbf-18a5-3794-9f14-7a40ad27dacc | -3.24252 | -60.8067 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 592ca839-dc1a-3fe3-a541-1a0f586d0bb6 | -7.86107 | -54.70507 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b801d58-48a0-3b8f-879c-6dba8a3786d2 | -5.99092 | -45.23705 | 2026-09-23 05:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e69bf8ee-e51c-33cb-b4b0-3f8968ea8b63 | -7.28187 | -56.46809 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d9466c32-ded0-301a-9ffa-88f4e9eb7863 | -9.05229 | -65.42159 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9a309a2-9bbf-389b-b782-2d0289534420 | -6.8197 | -59.46115 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4cf2d4e-4b82-3846-a11c-0a2b847b5108 | -6.6155 | -43.74834 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1969919e-43af-3cd6-bb13-d08b2ebdab4c | -10.71392 | -48.71687 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42316b73-8830-3655-a189-fab03a71c41c | -4.42778 | -55.08104 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3058eab6-4cb7-3f36-b00d-e69fb167a2d5 | -11.11661 | -51.05052 | 2026-09-23 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44ffe9eb-e59d-3d33-887e-c7594363bcc4 | -6.62124 | -43.74583 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c8e6c081-ecea-359d-a037-8896256446f4 | -10.56739 | -46.52362 | 2026-09-23 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06ca1d7a-58f8-343d-bdd7-a6c2bc063772 | -6.23851 | -51.00699 | 2026-09-23 05:04:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| af5f7881-c094-3947-8dd6-e644b3db5f3c | -6.32794 | -43.9355 | 2026-09-23 05:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 378ba83c-fc1c-3277-b22c-0fe3152c250b | -8.46321 | -48.68999 | 2026-09-23 05:04:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c0953c05-8e2a-3363-ab0c-90996f6f6f0f | -4.22336 | -50.66241 | 2026-09-23 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60bfa142-3e7f-3e2b-aa95-75a2cfba3a14 | -5.84058 | -52.00655 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eceb1776-249b-35be-89d3-644e696ca618 | -9.56009 | -46.53565 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f2c0744-e249-3c7b-bd05-506e9a3c538e | -10.00295 | -45.19965 | 2026-09-23 05:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 08b8b6a0-c77a-3c7b-ba02-daf628a9fa17 | -6.26213 | -50.81151 | 2026-09-23 05:04:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff310a4d-6cfd-3797-93c9-63f0f988a288 | -4.3737 | -55.27287 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b0549aa9-dd1b-37c2-bbd4-deb621381203 | -9.56922 | -47.95998 | 2026-09-23 05:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c53f012a-1aec-3e2d-b63a-def79e85de04 | -6.3591 | -58.28923 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04c33453-6c90-30f2-8937-5c6930225a20 | -7.8731 | -61.18124 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 91d42153-4630-3eea-b1d0-21e59efc13a9 | -6.60672 | -43.73396 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a60d497-9f1b-3672-b380-50fb58fd528f | -7.29052 | -59.53163 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe8d50cd-4a23-34bd-ba4b-238d9732f0b4 | -6.64896 | -59.92492 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 699523e1-3adb-32b5-9379-d0a169b5e290 | -8.10501 | -54.77474 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b23f4068-c664-3a4a-98f4-27454730e6c9 | -10.57198 | -46.52451 | 2026-09-23 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 298e7605-c953-3b91-bcd0-6011ec2a0b81 | -10.02699 | -45.20259 | 2026-09-23 05:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5d8da44-578a-3dc1-852a-496b8f3bfa1f | -6.13905 | -43.83862 | 2026-09-23 05:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31753c6f-5c51-3d97-a75c-b9a7d1298aa0 | -5.37202 | -56.05339 | 2026-09-23 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b7481ba-5880-3199-b913-cf33f87ce7e2 | -10.95237 | -54.09607 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2816edf7-60b3-3171-a29a-7288f6050eeb | -9.0446 | -65.4265 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ebe92eb1-cf8b-308e-8d09-e3209d9793f9 | -11.40036 | -44.04979 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f15f0f87-9bda-374c-b9d7-ff89c121f8c3 | -4.56562 | -54.92431 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cb5792e-4bef-3b9d-afa1-a7fb998857cb | -10.53732 | -43.98346 | 2026-09-23 05:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc76ed2a-46a7-3868-8206-baf39efce90e | -5.56685 | -52.02364 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a100c801-be8e-35ee-8c70-323ee5183349 | -6.32874 | -43.93215 | 2026-09-23 05:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8dc77271-2a3c-3e69-bc27-2180952b5af6 | -6.73192 | -59.42505 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ed4c14c3-49c5-3e03-8a16-65a49031de8b | -4.17618 | -53.667 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6169eb42-213b-30b2-a188-348abf502ea9 | -8.15116 | -49.55299 | 2026-09-23 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 098a56a2-920f-3196-936a-6bb5f6a9b1c7 | -6.4591 | -54.99597 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f82903e0-e84f-30f8-8fb2-f5fbb5462734 | -11.47758 | -47.35337 | 2026-09-23 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e06634b-5c1b-3bfb-a889-4d4be639e3b9 | -6.77552 | -59.63099 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e758c600-859d-3cf4-b791-c9dcb049bd95 | -5.50754 | -51.71439 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71290c93-6aac-3bf9-b1da-daf831f2e536 | -3.13948 | -61.39531 | 2026-09-23 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 605bc961-3352-3175-88cb-1801a248f6b0 | -7.32562 | -55.59227 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f11ece79-b358-37b6-8dec-2823c61a8f29 | -6.85774 | -63.01825 | 2026-09-23 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7f01718-ca4a-3126-94dc-1bf3009de066 | -4.52257 | -54.97165 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d5e7e30-b657-3f0a-bc9b-a9dc582ef4bb | -6.93007 | -46.55161 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0abb7dd-c03b-33a7-888b-0e8827e1426e | -11.12824 | -49.45018 | 2026-09-23 05:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 172998e7-8ec9-3fd4-b0e0-83a409c0ac3d | -8.30719 | -54.77694 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91b8e924-1f66-3541-bee2-50222eaf4805 | -6.78121 | -59.62992 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5df5f236-96bb-3c6d-b1a9-85b7cccee408 | -10.262 | -50.23709 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64a76b9a-93a6-30d3-82e6-25b354d74de5 | -8.91183 | -50.90125 | 2026-09-23 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41fb2cc0-695b-337b-ae24-56f1aebc0f48 | -4.41524 | -55.47638 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6024b021-d665-3574-b092-41eb1b2f5685 | -11.65707 | -50.9791 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1fedae22-51ef-39c2-8636-b687b9557ede | -6.73646 | -59.42579 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e01a724c-c4de-368d-bb73-b965d1f2bf85 | -7.57159 | -57.67718 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ca46b0e-f497-3daa-ad0f-829e1807f74d | -6.67115 | -50.94146 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c9b4a2e-8a6c-370e-ac2d-fa26a18d9064 | -3.78597 | -60.76067 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7df08691-ebd0-34b4-85ee-c93aa624f99a | -8.64821 | -62.49889 | 2026-09-23 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f0de51d-2e6c-36dd-90f0-82ad38a8dfbc | -6.30731 | -59.94685 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ece87d4-d50e-3635-b5b5-6d4fcb9c7aed | -5.80688 | -52.09031 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7230ca4c-7fa1-31c6-8b19-8da1726b5a12 | -10.2929 | -50.52754 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7df8d498-4cc5-3e7d-96cd-00447ad82e55 | -6.39109 | -54.88577 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README86.md)
