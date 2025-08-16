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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3805c23d-7c63-3d9d-b26a-0140c1c5fa15 | -6.5636 | -43.0592 | 2025-08-16 05:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| d8ec531d-1364-3c4f-9b96-12b480366361 | -8.9706 | -61.7224 | 2025-08-16 05:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 090eddce-abb7-3efd-ae1d-69b8ba74d495 | -9.1708 | -59.6568 | 2025-08-16 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| ef2fe8bf-f18a-36cd-b798-aed87b8fa296 | -7.9148 | -61.7478 | 2025-08-16 05:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 47131e1f-2941-32e8-89e9-5de5e59cab04 | -6.5638 | -43.0357 | 2025-08-16 05:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 0f87725c-3c47-300b-9b84-2ec5364ad8a8 | -8.9709 | -61.6842 | 2025-08-16 05:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 3c7e4243-0f3b-3b43-ad49-b9ec40d97234 | -14.9441 | -54.6959 | 2025-08-16 05:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 99aa6ee0-1b81-3171-a982-de53becd478c | -9.1709 | -59.6374 | 2025-08-16 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 5bbe50a6-1a87-32a4-a287-dde09dac4e0e | -6.9486 | -59.549 | 2025-08-16 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 291b12bb-a05a-3c22-9bb8-dd28422ea50a | -14.9628 | -54.7351 | 2025-08-16 05:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| e589536b-6d16-36ae-b84f-600b4e364520 | -6.9487 | -59.5297 | 2025-08-16 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 906a06d7-8827-3255-a4de-4bfb6bf8b34c | -8.9708 | -61.7033 | 2025-08-16 05:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 89d08a35-b8be-34b4-a59e-d76462db0461 | -6.545 | -43.0373 | 2025-08-16 05:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 23730c19-cecd-3644-99dc-d994963d4d7f | -14.9441 | -54.6959 | 2025-08-16 05:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| ec88a53a-93a2-32ce-8e5b-af12c04dad7b | -8.9709 | -61.6842 | 2025-08-16 05:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| b03f3cdd-c161-35b3-8e1c-691bc8fbec7f | -14.9628 | -54.7351 | 2025-08-16 05:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 87d4a98d-f15e-355d-9d6b-3eef9d0be54e | -8.9893 | -61.7024 | 2025-08-16 05:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 90988b83-d3dc-380b-b6b2-f6c83de42c81 | -6.9486 | -59.549 | 2025-08-16 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 41134ae1-4efe-3bdc-85c9-0d21df211ba0 | -9.1708 | -59.6568 | 2025-08-16 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| d30f4b2a-b110-36f2-b3b9-5e70496ae076 | -9.1709 | -59.6374 | 2025-08-16 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 4e056f44-b993-360f-8cd3-f582081165f0 | -6.9487 | -59.5297 | 2025-08-16 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 99c0cad0-4f28-3fe4-b672-3b6f17ec8fa7 | -8.9708 | -61.7033 | 2025-08-16 05:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| c6cec0e8-a0d4-33c6-8692-68e420455705 | -6.5638 | -43.0357 | 2025-08-16 05:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 2d5ce2af-cbde-311a-80ef-496455583bbf | -14.9441 | -54.6959 | 2025-08-16 05:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 1ccb59ce-0455-3a04-a2a1-6a0ffec022a4 | -8.9708 | -61.7033 | 2025-08-16 05:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 164b101f-5aad-381c-a8fc-d70b66cfd725 | -6.9487 | -59.5297 | 2025-08-16 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| f162b8e6-3f33-39f2-b0cc-8443b21082de | -8.9709 | -61.6842 | 2025-08-16 05:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ddc82a87-044a-38a2-8bc4-4eca86608551 | -9.1709 | -59.6374 | 2025-08-16 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| b5b2a736-b8d7-32a7-8e9a-dcefef5b8573 | -6.66412 | -58.81432 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3c93242-ec8d-345c-9a0c-0328d8c68f8f | -9.3989 | -60.5431 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5b97985-714b-353a-8adf-aa468f116245 | -8.99081 | -60.53254 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 177bd15b-d995-389d-ac8a-21fdcdac995a | -9.16734 | -59.62496 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fbb22814-6eb0-39d6-8f08-6283a20576cd | -6.66742 | -58.81966 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c84d7062-cfe7-33a0-8094-38799d4bc030 | -9.18155 | -59.66576 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0daeda82-180d-32ec-a62a-777d8c5f20a6 | -8.98091 | -60.50255 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1083258d-3a51-31d7-89d0-98752f69ccfc | -8.46984 | -64.0488 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0413bf85-9c00-3662-9341-55ea12a13bb9 | -6.94372 | -59.52687 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f03245e7-6ab8-395d-94bc-b39740cfc307 | -7.87891 | -61.82365 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5bed3a4-b6b1-399b-8619-0c09589318e6 | -7.56299 | -61.42295 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd128a04-d474-3dc0-adc0-f0417652dd1e | -9.1544 | -59.68341 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7676dc9-57ec-3b23-a983-0382d2a854bc | -7.44059 | -60.0203 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f936ad69-9dc7-3e34-9fd4-80825f3239fa | -9.16289 | -59.65746 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d74b464e-7756-3f48-be05-0fbd08cc0f40 | -8.98878 | -60.51322 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 127886dc-2c84-3018-b08a-ba0be0317f76 | -9.49947 | -60.55891 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bfbcd5af-2b25-33e0-a5ca-8194e25ef065 | -9.21256 | -59.63793 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2eba72a-b0ba-3f1d-9dfe-6df18aa3591f | -7.45416 | -59.9375 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9945a3d1-f1da-3378-bc73-4cfcc45bdb6e | -6.65669 | -58.82381 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c806e99d-ec86-34fb-a62b-b01601e20e40 | -7.87229 | -61.81133 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 995c24cc-4971-303b-9621-ed341bea4f87 | -7.41501 | -64.61425 | 2025-08-16 05:50:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe8c0ac0-7e30-30a1-95f5-8775919aa6ee | -6.94772 | -59.53269 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e5915cb-e51e-3fe0-a784-78df17f1d427 | -9.51064 | -60.54611 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ad008358-9dd1-3183-8b07-55d8dc62bb7f | -6.14503 | -57.9363 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f282a041-b644-38cd-ba66-6294d1917d8a | -7.53461 | -61.34898 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fee572c3-acd7-3203-b9f2-f13d4cace591 | -9.20208 | -59.64221 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a68e07a-4ca4-3455-96c4-c7d7d717f05c | -8.98503 | -60.50475 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 108f839d-2b27-36ee-ac77-e2a98d10d433 | -8.5555 | -63.92649 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cd6f330-2eec-3c6d-82f5-c810975110b8 | -7.94761 | -63.22169 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40383828-853f-3439-b2e0-0956c782d9d5 | -7.43702 | -60.02296 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b92dd56-e9a0-3f69-8d62-abbdf9d84b62 | -9.20249 | -59.65755 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 242d80d2-b6e1-3cac-9080-fcfc9a165f5f | -9.21458 | -59.66004 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6c6750a-bc44-3398-a9c6-0efebc75ea13 | -7.52957 | -61.32426 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53f6f473-9842-38ab-ba82-d7740f8a1458 | -7.91544 | -61.74598 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d89c48b-ee79-3512-8fe6-efa09c585083 | -7.91443 | -70.22426 | 2025-08-16 05:50:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09a0a334-101b-3238-9eb4-b398ae7a048b | -9.5041 | -60.52607 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db75ffbc-5c62-3ac3-9974-27eaa11194fb | -7.87175 | -61.81504 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ea6acd2-42da-32e0-aedd-76e6c25914ce | -8.99992 | -60.53393 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f99f65e1-9402-3361-96b1-aea39fb7d196 | -8.97375 | -61.68338 | 2025-08-16 05:50:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad10fe8f-e7eb-313b-8281-b1f463c8cfee | -7.94601 | -61.75443 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e4b2f6f-deba-3aa4-bcad-76bdb09ca42a | -9.50343 | -60.53078 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 144e6a8a-a054-3487-8140-3451370a31ee | -7.61226 | -63.32544 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cb31bb7-66d2-3c3e-b614-82dd461ef11d | -9.15996 | -59.67884 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 062d8ef3-6375-3e00-82ac-7230a059813e | -8.69868 | -63.96359 | 2025-08-16 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0e80cc9e-dd85-3fb8-9b15-e8966dfe353c | -9.18378 | -59.6496 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff76e5e3-0396-30f8-943e-5b4ebb2fa87d | -7.25089 | -57.62605 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d8984c6-3a7d-3408-8730-add15ec554d0 | -6.13505 | -57.92868 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbadf478-4818-3108-9476-34ad61c41e99 | -7.87838 | -61.82732 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 570f85d5-a077-3027-8c06-65f2fd80e736 | -9.00118 | -60.52472 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 229f5332-ea4b-3591-9d41-129f4090f301 | -8.55916 | -63.92704 | 2025-08-16 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8f54749-c1ea-34c6-8a66-1803bea6a8b0 | -7.61141 | -63.33658 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c334d257-48d3-3ca3-b4c7-1d937fbb1700 | -7.52591 | -61.37922 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d52c2da5-2968-365e-81de-8942a972a447 | -9.18905 | -59.68299 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2150a033-0c60-39fb-baed-553f1ee43cd9 | -7.94961 | -61.7588 | 2025-08-16 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbca7048-c514-357b-ab15-d4760891aee8 | -7.07381 | -59.22977 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbbf2160-8283-36e0-9211-75b2bd01a657 | -9.17147 | -59.63103 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5cf90d8-eb01-3e5f-8c0d-2c7c17823a15 | -7.68324 | -63.31542 | 2025-08-16 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e6b9ce6-ea56-333a-ae42-0a4e8c38a1f4 | -9.50931 | -60.55549 | 2025-08-16 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d10a7e7-71a4-3c65-9d66-7ca49cd6f1d9 | -7.28153 | -57.65796 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46702c17-0f72-3d3f-92de-7c60ba4b49fd | -8.98436 | -60.50943 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 586cbe17-a6cd-3036-8f89-66c04fa72bb2 | -6.87459 | -59.84323 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f93e785-23b4-3bd3-987d-a93231d0dd4f | -7.82156 | -61.32672 | 2025-08-16 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95f6711c-0bbe-3987-8038-05a45563ef96 | -6.13979 | -57.93565 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f2604fa-4f71-3e2c-ae26-02917cb89ce4 | -8.8914 | -60.74274 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be00f7bd-02a0-3bd8-a790-5e6b884f8879 | -6.94699 | -59.53776 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d3309ca-8568-3551-8053-40e8b41b18b0 | -8.99281 | -60.51546 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 71f85915-929f-36d0-93a2-0c11bb2dfbcc | -6.13497 | -57.93186 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3257a81b-294d-36ad-baff-c0cca6bbc6e2 | -6.94065 | -59.64851 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b87e6a34-5a74-3387-970f-d711e77c162f | -7.24546 | -57.6253 | 2025-08-16 05:50:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b88cd944-0426-374d-9b39-e0d61c53e696 | -8.98112 | -60.49945 | 2025-08-16 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7db480bd-e68d-3f04-acc1-96404de27838 | -7.06823 | -59.23429 | 2025-08-16 05:50:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2289dd9e-7b62-39e0-8722-2617c2b57419 | -6.65343 | -58.81845 | 2025-08-16 05:50:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README64.md)
