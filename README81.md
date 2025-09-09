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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 106f1f50-3d02-3314-9ca9-cc5c394bfa88 | -9.8266 | -46.0322 | 2025-09-09 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 5e07207e-53a0-33e9-8fec-cd5ee3e7632e | -17.7322 | -44.4879 | 2025-09-09 13:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 93.2 |
| a3173e83-b53c-3d93-8ff9-4383072c2b90 | -5.2263 | -43.7006 | 2025-09-09 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 412b1aee-df17-3a34-aa6d-c27154a28c4f | -12.0295 | -51.0935 | 2025-09-09 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 9242fe2b-aa92-35fd-8186-7831ef5cea31 | -17.7328 | -44.4637 | 2025-09-09 13:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 606ed8f8-ab48-3049-90dd-94c0aae6b0e3 | -6.3469 | -44.0551 | 2025-09-09 13:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 901e2841-8f58-3edc-82ca-e92345c57f27 | -5.7168 | -45.4035 | 2025-09-09 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 2aeabab0-265e-373c-8db7-6b6b1ee65e67 | -15.1049 | -48.0434 | 2025-09-09 13:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 123.6 |
| e62144af-d22b-3c01-8dfc-18588d913bc0 | -9.2101 | -59.3833 | 2025-09-09 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| af009ffa-c635-3549-b3c0-1c5c7ad57a80 | -6.2595 | -43.4129 | 2025-09-09 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 086258a6-ee8d-3e46-befa-4dbad7d1e854 | -4.7346 | -44.4457 | 2025-09-09 14:00:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 3f4598c5-b3a5-3c32-b83c-212c19e65868 | -11.4465 | -43.6224 | 2025-09-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| bd1b0625-33bf-3ea8-ab01-e58a5c80a1f1 | -15.8201 | -52.2659 | 2025-09-09 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| c463fc78-f6d7-38bb-b5aa-c6d2d1e9b7f2 | -11.4482 | -49.2704 | 2025-09-09 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| abee94cf-3881-3a19-947d-ed8080579197 | -5.0438 | -43.1314 | 2025-09-09 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 42aa1d4a-0d6a-366a-8b3e-9a10a34001a5 | -12.1991 | -53.8817 | 2025-09-09 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 344.6 |
| 437b14ed-5b90-35ca-8cb8-f3caae00b1f4 | -11.446 | -43.6461 | 2025-09-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| f57a90d0-9a5b-3243-9021-1b242ebf208c | -6.3078 | -44.2196 | 2025-09-09 14:00:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 581102b0-3bdc-3e8d-9c10-41cd6a569f3d | -17.2973 | -46.6799 | 2025-09-09 14:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 8841eff9-4d96-3aa1-bcc3-9b9106fe9483 | -11.4272 | -43.6254 | 2025-09-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ebcc8a2e-0a58-3460-a536-05aaaac0d553 | -12.6343 | -56.9725 | 2025-09-09 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 56731100-6c5c-3e17-b3fc-744679489c7b | -8.4119 | -49.0869 | 2025-09-09 14:00:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 187.6 |
| ca2cf2f2-ea2a-3700-9c31-56acb16e6288 | -19.9545 | -49.2928 | 2025-09-09 14:00:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 150.5 |
| d52d2f2a-eb2c-3547-8466-41fff713ca80 | -5.2263 | -43.7006 | 2025-09-09 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b68da0b7-b58a-38c4-80ad-02d23844e419 | -11.3172 | -50.4275 | 2025-09-09 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| fccdcc3b-8fa2-3bc2-8a94-31846b5121f7 | -8.0606 | -48.6423 | 2025-09-09 14:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 69cd2b36-d021-3e5a-9e71-1f7146e3afca | -6.3469 | -44.0551 | 2025-09-09 14:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 9d18c42b-8f17-3f8f-b331-a208be5bfe33 | -17.2762 | -46.7305 | 2025-09-09 14:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 43aa0a7f-4c64-337e-9eca-2d9e14a1735b | -13.9723 | -54.0419 | 2025-09-09 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 1ffdc321-bf9f-3db6-abfa-ccf6789d6915 | -11.4281 | -43.578 | 2025-09-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 488201de-5d32-3c75-a17b-217109632466 | -5.8406 | -44.0951 | 2025-09-09 14:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 7f270ad3-5618-3c4d-b953-d12f53cb4f6d | -13.9726 | -54.0211 | 2025-09-09 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 1fe74fd1-e208-3bfb-886f-82af3de83ea4 | -6.199 | -45.8186 | 2025-09-09 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| a05e0579-778b-3c50-a690-6a35f8422b3f | -7.789 | -46.0891 | 2025-09-09 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 23e543d0-75c8-33e0-ae1e-c3a5780d65e9 | -16.3403 | -43.0394 | 2025-09-09 14:00:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 121.7 |
| f4316c63-b78e-37d4-bb93-5dad29911cce | -11.4506 | -50.3912 | 2025-09-09 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| f1c76cfe-0297-3254-8493-3c5324900a9b | -9.7017 | -46.8323 | 2025-09-09 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| b8cc4b74-c1d2-3465-b430-07feb527b22e | -11.4277 | -43.6017 | 2025-09-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 607f7507-f058-3116-885c-a625dfddd1c8 | -8.0604 | -48.664 | 2025-09-09 14:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 79.6 |
| a83824e5-3f8f-3c33-8557-7e091a6507bf | -12.1993 | -53.8611 | 2025-09-09 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 67fd30f3-62c3-3a2a-9ea6-bc3bdc756091 | -17.2557 | -46.7578 | 2025-09-09 14:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 61022c28-fbd4-3a6b-8481-d2d0cebfe905 | -17.7322 | -44.4879 | 2025-09-09 14:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 672791e0-2aee-364c-9f46-fbd427612b6b | -11.3011 | -46.5244 | 2025-09-09 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 234.2 |
| 48d9a327-49e8-3978-81b5-35dcdd53648d | -6.3223 | -44.6542 | 2025-09-09 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 26817bf3-acbf-3410-b02b-ca54dd643c15 | -12.0295 | -51.0935 | 2025-09-09 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| ecf9a55e-7df3-3033-b801-003b9a042ef0 | -9.6289 | -48.0129 | 2025-09-09 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 0a5bfc38-3845-36be-9c81-80ed332780a8 | -16.3602 | -43.0349 | 2025-09-09 14:00:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 231.7 |
| a90fd570-16a0-3588-9a47-13cb60449412 | -9.7014 | -46.8547 | 2025-09-09 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 9fe01758-1669-30cb-ba3a-10fff7465b29 | -11.3552 | -50.4233 | 2025-09-09 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 1fec3ec4-7f05-3982-80ac-17b5be802a1f | -5.3482 | -44.7943 | 2025-09-09 14:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 9a090d74-af13-3336-b1bc-a4337db22812 | -6.2224 | -43.3693 | 2025-09-09 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 2c7e36b1-684d-3962-a79b-2d15d00813c4 | -8.4116 | -49.1085 | 2025-09-09 14:00:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 171.6 |
| d799f241-998a-33ab-b55d-305372ef7dc8 | -9.2101 | -59.3833 | 2025-09-09 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e0be3594-cb28-3f08-b3ad-a094442a5374 | -17.7328 | -44.4637 | 2025-09-09 14:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 226.0 |
| a7294359-789b-359e-b873-a28976bb74b3 | -12.0291 | -51.1149 | 2025-09-09 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 368be497-c92f-3a58-9523-6a0c6288de5d | -17.7127 | -44.4684 | 2025-09-09 14:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 5eda52fb-3397-3524-ab55-3714aab77768 | -12.18 | -53.8836 | 2025-09-09 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 0448dcba-f3ec-3094-ae7c-b6de410977da | -5.4587 | -42.797 | 2025-09-09 14:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 181.5 |
| 212e0bea-9877-311d-9453-328eccc18502 | -15.7583 | -53.5268 | 2025-09-09 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 31033e12-3465-3baf-b5e7-66f8788f40ad | -14.2932 | -45.0261 | 2025-09-09 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 6814841b-8fbd-3824-9d18-5c96bd18ffc9 | -9.1914 | -59.3843 | 2025-09-09 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| ead5636a-bafb-3da9-b8d9-9dc9d252be24 | -8.4612 | -51.4595 | 2025-09-09 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 35769143-cedc-3358-921e-7d1a5f09b62b | -11.3014 | -46.5018 | 2025-09-09 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 8193864f-9031-3821-8710-6d72047ba152 | -7.7107 | -44.7369 | 2025-09-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| df583e59-97db-3a53-9d71-6f1536c6a311 | -9.2181 | -60.8305 | 2025-09-09 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 25c96f5c-de4f-3dd1-8f36-e27df870271c | -4.7345 | -44.4685 | 2025-09-09 14:00:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| ddb2031d-939b-3639-8a76-a7476a53dd81 | -17.2967 | -46.7032 | 2025-09-09 14:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 3bb772d1-ccf6-3340-a5d1-f268e45b8c00 | -5.589 | -42.9048 | 2025-09-09 14:00:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 468.3 |
| a7850458-cd6a-383d-8132-bb0e30f8dc84 | -6.3467 | -44.0782 | 2025-09-09 14:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 673e04f7-a800-343c-a15a-042ae60ec76c | -5.8791 | -43.9769 | 2025-09-09 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| f4420d29-c159-3ced-800a-60660ba7f4f2 | -5.8397 | -44.1872 | 2025-09-09 14:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 2923fa09-5cf6-376e-86d9-c30e54aa2bd5 | -5.348 | -44.8171 | 2025-09-09 14:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 5db5bc7b-bf6c-3911-a92c-ce20e08d481d | -11.2007 | -54.9992 | 2025-09-09 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 7069d8e2-aaec-3467-9cd1-7c9ca42f45b8 | -9.7857 | -46.24 | 2025-09-09 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| c157b522-381c-3e53-876e-899720bb7962 | -11.3389 | -46.5419 | 2025-09-09 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ca3d0a23-3732-33ec-9f1b-752c9ef076f3 | -12.2178 | -53.9005 | 2025-09-09 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| b58266ab-24f2-33dd-a6b5-206efef83523 | -11.3385 | -46.5645 | 2025-09-09 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3d47e465-68f6-3b72-b071-8718683c9bb4 | -5.9563 | -45.7915 | 2025-09-09 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| da289ecd-cea6-3bbe-afaa-7f4459d7aac7 | -13.1367 | -54.9171 | 2025-09-09 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 7eb26eeb-4fe5-31de-b2e0-89cadaf26e9f | -5.6418 | -45.4312 | 2025-09-09 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 49871c14-d2fe-3f96-aaec-9f0475ff315a | -17.5799 | -49.8019 | 2025-09-09 14:00:00 | GOES-19 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 676df71f-49b5-3c99-b5d0-2227162de5bf | -5.7168 | -45.4035 | 2025-09-09 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c6ba6f30-0069-3a69-996e-b6c4b5017075 | -12.1988 | -53.9024 | 2025-09-09 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 230.9 |
| 2565709e-4feb-3a5f-b1df-9dd3d31ff906 | -5.7483 | -43.9406 | 2025-09-09 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2baba9c8-6146-30a7-a540-cd74dc3a73e0 | -15.7775 | -53.5454 | 2025-09-09 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 175.6 |
| f569e426-b30a-3c04-91ab-c87633affa9f | -7.5407 | -48.2303 | 2025-09-09 14:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 7d39628b-70d5-3739-a628-d373aab9123d | -9.7203 | -46.8526 | 2025-09-09 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| c3325ea7-ea85-3e24-ab15-89c5f79db6f4 | -11.9726 | -51.0788 | 2025-09-09 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c06d29cd-b793-3426-88d8-a49fc9ae36ba | -5.8582 | -44.2088 | 2025-09-09 14:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 54cb1165-a3e7-3519-b6c5-f2020f9b68b3 | -7.5611 | -44.6597 | 2025-09-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 5f4a5f92-7015-31ba-bbd9-58b79d0ec65b | -7.5799 | -44.6579 | 2025-09-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 210.9 |
| 5c588139-02d5-376e-b50d-138db8230b82 | -5.975 | -45.7901 | 2025-09-09 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 98632e41-d6b6-3faa-bf31-54306a5a7c73 | -9.7206 | -46.8302 | 2025-09-09 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| c509386e-b090-32ab-8984-5adda7ed7b06 | -8.3929 | -49.1101 | 2025-09-09 14:00:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 90c2a70f-b355-3366-8f04-33208a7cb9fb | -11.7706 | -50.5901 | 2025-09-09 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| ac373425-3f45-3a8c-9cd3-b23f7384fdd3 | -11.3549 | -50.4447 | 2025-09-09 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 184.0 |
| a42c5876-07ac-3fbc-bdd0-4da83144782e | -12.6153 | -56.9742 | 2025-09-09 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 5286b0bf-e19d-3e61-8786-df4bfe0d8f20 | -5.8218 | -44.0965 | 2025-09-09 14:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| a5cf22ef-d259-33ad-9f08-f7391de2e679 | -5.2265 | -43.6774 | 2025-09-09 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 7caccbb0-88f2-3c6a-958a-d62b2f14540a | -5.5506 | -45.1664 | 2025-09-09 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |


[Clique aqui para ver as próximas entradas](README82.md)
