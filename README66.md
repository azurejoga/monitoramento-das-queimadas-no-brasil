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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b576e33f-e94a-36fd-bcf1-01723dbfe395 | -1.19937 | -54.11957 | 2026-09-15 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b46ea29-9f75-3b34-a561-2c90030228fc | -6.02011 | -59.92903 | 2026-09-15 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| afc172b3-ba2e-3746-85e9-75352f08ddb3 | -6.1135 | -57.67286 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18573486-ad6d-3517-b2a2-0ff5eabcb0f4 | -2.68379 | -57.59124 | 2026-09-15 05:53:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d73b64c-2434-37df-b90b-4b032f462f43 | -3.54326 | -53.99393 | 2026-09-15 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 14aee238-4814-30ab-9016-ef1df299363f | -1.23199 | -54.09717 | 2026-09-15 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9c175a2-3f4e-3a63-abe4-27bf042fe644 | -7.55761 | -62.33009 | 2026-09-15 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8936575d-61a4-3737-97e7-61b30d6a1909 | -6.11131 | -57.6886 | 2026-09-15 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9093c60-3203-3223-be4b-e83ea5418e7a | -10.67892 | -54.16462 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2791d753-1668-355c-9887-ee0e693ac6ab | -3.74655 | -61.75627 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f65e40bc-b797-3ad7-8ac9-ddec964251b2 | -10.67506 | -54.14198 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30efe393-2526-38cf-84fb-808d9b87153c | -4.53457 | -55.62345 | 2026-09-15 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9857e28c-3d47-3901-a922-e30a878eb83d | -3.69646 | -58.88148 | 2026-09-15 05:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e501479-18c2-36c2-b214-9975ef051302 | -3.12856 | -61.24747 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87ba2e2c-4025-3fe3-a2cd-eb0407b2692c | -9.69683 | -58.17694 | 2026-09-15 05:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf42285f-281c-3c7f-b2b8-51b901951307 | -3.07834 | -61.5269 | 2026-09-15 05:55:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ef2982d4-92bb-388a-8fc9-a153fd7821fd | -9.85136 | -65.1841 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf132e40-c55e-3965-b148-a0e8c7cbe738 | -10.66983 | -54.13063 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3593b14-e559-3af5-841b-b875680eee1f | -5.81122 | -53.80415 | 2026-09-15 05:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7b80f23-ebfd-3d5d-be52-993b4488d022 | -5.3594 | -55.89528 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5098bc21-cdd1-33ea-bd5a-b57ab61c8fa4 | -9.40944 | -62.70739 | 2026-09-15 05:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| df984f31-b522-356b-a8f7-3e5e5e66f8fd | -5.92787 | -53.54892 | 2026-09-15 05:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a60dc64f-c317-3247-bc10-0d2cc6ccb0c8 | -3.12088 | -61.41887 | 2026-09-15 05:55:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f3a15a53-e280-375e-9e97-a1bc4be87724 | -5.35399 | -55.89463 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be2c3c1a-7843-3879-a3d2-fb7c8e3d58fa | -9.58948 | -60.51478 | 2026-09-15 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97a5fe93-e5f3-3da2-ba28-934db36d0b35 | -3.7364 | -61.75051 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39e599bd-6816-3b77-b981-b6d77b55e6dd | -9.25956 | -59.64011 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44a25214-965a-3ae2-aab4-155114dba0fa | -9.85528 | -65.18107 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cd8c74e-c27f-37d8-94ac-0c40f9db429d | -6.15807 | -52.79409 | 2026-09-15 05:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c28182d3-23b1-3da7-81d4-11b46981fd0c | -5.1327 | -55.95008 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e619ff75-de1f-396f-810f-951efae45531 | -3.91369 | -54.51987 | 2026-09-15 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfb7e8cb-e244-3484-93e0-146647845b94 | -9.2072 | -65.6212 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28862186-6775-3a47-b4ce-60f1658ffce0 | -10.60684 | -57.31773 | 2026-09-15 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 010767b6-71ee-3c6f-bca1-6a9a9135a8d8 | -12.12787 | -57.18647 | 2026-09-15 05:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 882296ef-fa54-3c52-9314-5dd139a5c987 | -9.12802 | -65.84165 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21b113ec-5bde-3019-8c25-6de580c4ba26 | -3.72085 | -58.86473 | 2026-09-15 05:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a659da7-1470-3181-8d79-f28af8f6adff | -10.65771 | -58.76514 | 2026-09-15 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e81e468-4931-3d9d-bde7-d3319c21a12e | -3.42907 | -58.21517 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ea0f7bb-0c58-39fe-a75b-669ce7348be2 | -5.8119 | -53.7994 | 2026-09-15 05:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49beda0c-6071-3287-af95-44339502a0e7 | -8.81709 | -62.49123 | 2026-09-15 05:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef54201d-e39f-32ee-a564-723985532a47 | -3.91949 | -54.52061 | 2026-09-15 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2298b94f-fb4e-31b6-abaa-02a97e08a6f2 | -4.52354 | -54.91925 | 2026-09-15 05:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20d6cea3-ddbb-383b-ae8c-7470b903a49a | -9.68722 | -63.42942 | 2026-09-15 05:55:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8749bb28-c735-3a34-8f57-98755e622818 | -9.71121 | -64.9239 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc5b5c5a-6631-39d6-91b4-d5a8e3d3aa74 | -10.60114 | -57.32018 | 2026-09-15 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29f93517-d4ad-3daf-a46d-6b7f63bdc936 | -9.98603 | -59.87087 | 2026-09-15 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5575f5c-a6f7-3c5c-8b1d-cd777cce7bae | -3.60033 | -59.06836 | 2026-09-15 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86ea20f5-b654-3b86-a717-ec1016d3e6c1 | -9.13246 | -65.83519 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8c713d0-e540-3ffb-9352-41c5dcbc65f2 | -3.12424 | -61.25117 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c272e271-dba1-3a4b-8556-dbd42d3ff33e | -9.10176 | -65.56152 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| daa48c87-ddf8-379f-bc68-9241c2018ac2 | -9.12137 | -65.84058 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7a47d6f-9559-3817-8427-6e32e9d8f3bd | -9.1247 | -65.84112 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc0b9f4c-d58d-3ff9-85a8-285bb3945da7 | -9.85192 | -65.18053 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bd0a911-dd56-3f7f-acf6-e7db8d64e3a6 | -10.66919 | -54.13594 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e04362e-5a8f-386e-a96b-685f402bdedf | -10.25862 | -57.69793 | 2026-09-15 05:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 582a1746-796a-3ef0-8e19-b29753f15aa2 | -5.13368 | -55.94326 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd86b789-9c9c-3ff2-a8ff-6bc049d77988 | -13.39745 | -57.02599 | 2026-09-15 05:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| def980bf-aae5-3c52-ac88-9fcac48bcceb | -5.12888 | -55.93857 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0951e0b-9093-3f52-a02a-ec74c8917b07 | -3.75078 | -61.75272 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a960ba17-c484-3e40-9c1c-c3d00499abc2 | -3.35156 | -59.83213 | 2026-09-15 05:55:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05017a3b-2285-3a76-8296-a0f26f1c574f | -9.07231 | -61.01375 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0365f05-9582-3377-9868-b3f1b467e29b | -3.12674 | -59.03608 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 794fc457-9c48-368e-9642-15178d9ed785 | -10.66252 | -58.76566 | 2026-09-15 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c136b5f-1537-3b87-a39d-75cbd864e53c | -11.26785 | -54.12539 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99ed2c21-10eb-37b6-a69a-11e7adf2fa39 | -9.07283 | -61.01024 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2deff12c-53bc-31e2-8b95-12e33515fe6c | -9.13689 | -65.82874 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03d63d60-b0bb-33dc-b55a-4c31feae46c6 | -5.81922 | -52.10284 | 2026-09-15 05:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38f1a95b-e491-3cb2-8a5e-9b6ec178d9cc | -3.73767 | -61.7423 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcaecca7-9e01-3bca-b492-4b94e83673c3 | -3.17909 | -61.11464 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30e35252-52ca-3ed5-95ef-1cff83052fca | -3.75014 | -61.75682 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0550e32-efd9-307a-b8d7-3fc5980f3c23 | -9.01505 | -61.01233 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3547866d-3546-36eb-addc-5417179c2d2f | -3.07687 | -61.07878 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad436aa7-a4ca-32ec-bc1c-4e81bcde16b7 | -5.13418 | -55.93976 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a09e7d3-5df7-35fc-928c-93ffdbf0fd00 | -12.12198 | -57.18926 | 2026-09-15 05:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 864d352f-e6a4-3daf-b27b-e9ba4a749f84 | -3.12615 | -59.03989 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38e0edf4-d1af-3792-894b-de403aa4f89d | -3.74127 | -61.74285 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b2ceb11-4eda-34b6-bfed-3d05f6adaac2 | -3.41882 | -58.22254 | 2026-09-15 05:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 502bc698-b336-30c5-99f6-1141a1492f3e | -9.41549 | -62.717 | 2026-09-15 05:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c87cf3f1-24ad-32a4-b544-2e4bf8dd34e0 | -3.7495 | -61.76091 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e2cc6f6-d030-37e5-b0eb-7328da7b590f | -3.17473 | -61.11841 | 2026-09-15 05:55:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e22cba2f-ba67-3f0c-baac-1a46cbf34a56 | -9.1319 | -65.83868 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4db04ea3-ecd4-3674-8529-bbc959469a80 | -5.12837 | -55.94217 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18c97c4e-fe25-3031-80ee-3843ec9b0e1d | -9.10564 | -65.55855 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 275bdde0-c883-352b-9092-75581e98dad7 | -3.73703 | -61.74642 | 2026-09-15 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad8f05ee-2eec-3b8b-b963-135d60ba9d2f | -13.39791 | -57.02211 | 2026-09-15 05:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1013042-4b54-3e23-82f0-53b892501543 | -3.69705 | -58.87746 | 2026-09-15 05:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54987047-6596-30ea-9f5c-bcbf953fbfa3 | -9.13634 | -65.83223 | 2026-09-15 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 430f2a01-efd6-393b-82bb-9e3035f90628 | -10.68409 | -54.17622 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb30b968-e9a7-3b84-b730-056eeff3880a | -9.6899 | -63.4292 | 2026-09-15 05:55:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9351688f-f7b3-336c-bc56-ff5861781884 | -10.03586 | -52.09086 | 2026-09-15 05:55:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8a7c82e-b5eb-38ce-a2b9-8795b16b79c5 | -5.16391 | -59.76805 | 2026-09-15 05:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f07d336f-1be9-3029-8a47-c014f31e5d5a | -5.12689 | -55.95249 | 2026-09-15 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06739f7c-0704-3afe-9ef5-2ebca577e4f9 | -9.01957 | -61.00944 | 2026-09-15 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3495246-5ef1-3ff1-90b3-3df81ae3c9ce | -9.53101 | -63.62495 | 2026-09-15 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f759ef9c-9425-362a-a8a9-0a5078c102c9 | -9.96829 | -63.97376 | 2026-09-15 05:55:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92a02132-ef40-3425-b44c-978317711ba5 | -4.38257 | -55.20139 | 2026-09-15 05:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d794142a-41c2-30f1-ba0e-0c6b7b6ba14a | -10.6744 | -54.14742 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1df15da1-733f-348e-b87f-3d60ae9a3f76 | -10.69121 | -54.1717 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fdf9777d-f986-38bf-8d7f-44780b598ce7 | -10.6757 | -54.13659 | 2026-09-15 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 677e85be-8908-3742-891b-025a4265aaf9 | -3.52291 | -59.06564 | 2026-09-15 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README67.md)
