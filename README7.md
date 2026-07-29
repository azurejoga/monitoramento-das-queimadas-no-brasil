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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fdec419-4b48-365c-81b0-4696e2a03741 | -14.06137 | -53.96714 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10fd2a8a-fb7b-3863-9f94-b5cb56108243 | -14.03204 | -53.98207 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6b0365d5-889a-3b4f-b8ef-6df17fc2f9a7 | -11.53173 | -47.56638 | 2026-07-29 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6e5ea6e-7fa0-3e51-9726-4e31e30f4001 | -11.53259 | -47.5617 | 2026-07-29 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19806578-73e5-3d41-b544-813703f6efa3 | -11.52856 | -47.55822 | 2026-07-29 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ffb1e47-7388-3d8c-918e-0e722afa58fb | -10.92987 | -43.05335 | 2026-07-29 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6854f801-8b90-31f1-87d4-2835dfe44913 | -15.17626 | -43.85306 | 2026-07-29 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef885a02-4dec-3c99-9490-a719b30e2c4f | -15.87177 | -43.60056 | 2026-07-29 04:14:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ce6ac21-68b2-33d4-8497-053f38e165fd | -10.32257 | -49.71319 | 2026-07-29 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c231190-924f-384f-a388-65dd70c61072 | -15.32943 | -43.02264 | 2026-07-29 04:14:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1fa5b518-50ad-3ca1-850a-0f00917d8551 | -9.61199 | -47.76793 | 2026-07-29 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41faf6ba-bd1e-3a7d-8163-1cc25ebcea66 | -15.8785 | -43.60173 | 2026-07-29 04:14:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58c929ee-e150-3637-a60d-0dddef7f624d | -9.66092 | -40.5965 | 2026-07-29 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 4fa84674-7de8-38d9-9def-aba97e06ea46 | -10.13429 | -42.4217 | 2026-07-29 04:14:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5ea48cf5-c464-34c4-a731-0b4a611a53ce | -14.03312 | -53.97692 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eabea492-8c17-3efe-b1c3-aed1971e69b2 | -9.66479 | -40.59354 | 2026-07-29 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 81edfaff-1b92-39fd-a609-7e1d14170215 | -9.33955 | -47.32101 | 2026-07-29 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 740a6700-14ae-3b36-a9fe-7f158f57d6b9 | -11.26625 | -49.55779 | 2026-07-29 04:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1cfafb5a-2426-35f8-9c0b-04a70b88853a | -11.51692 | -47.54785 | 2026-07-29 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ab02e22-00dc-3475-8d62-014d17271eb7 | -11.52933 | -47.55387 | 2026-07-29 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9aaa8e89-7b4b-3b91-a8d3-8c39b0303630 | -10.36305 | -49.75316 | 2026-07-29 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 912af930-4ff2-3c77-b2d6-cb494184d316 | -16.05166 | -41.44554 | 2026-07-29 04:14:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bc2ae234-cf2b-3f6d-a977-3d9e193778ff | -15.43676 | -41.37934 | 2026-07-29 04:14:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2ce430cd-b7cc-350a-a4fc-83f79a2287d5 | -14.0707 | -53.98528 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a189ab20-fb52-3900-b593-1b31784046f1 | -11.52549 | -47.55145 | 2026-07-29 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f2dd9b8-fa50-33ac-8fe3-8f4a3bbb7872 | -10.9361 | -43.05827 | 2026-07-29 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 0a55b0e0-20b6-398e-b221-29e5e11fb8d9 | -10.35277 | -49.75116 | 2026-07-29 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abf5aff6-8160-3cd6-92a1-1057f6da7a98 | -12.45172 | -47.89181 | 2026-07-29 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2229078e-d019-3c9b-bdba-553e97c3440e | -13.45689 | -44.04617 | 2026-07-29 04:14:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2dc3154-2f49-3527-8d06-81d3e50ea147 | -10.92925 | -43.05711 | 2026-07-29 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a77e9cea-f2f9-3cf2-8409-0c9dfb05c648 | -14.02057 | -53.97424 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef249f7b-adb5-3f34-815e-d367535c72a5 | -10.35791 | -49.75216 | 2026-07-29 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2791f1e-e0ae-31b3-a136-67fac09896ab | -14.73069 | -47.13858 | 2026-07-29 04:14:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8b83d2f-c786-3582-b3b2-4eac573b711b | -11.93386 | -45.52917 | 2026-07-29 04:14:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bbd5956-fd5d-3721-8ab5-9ed273142b72 | -9.1009 | -50.60911 | 2026-07-29 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b547bd3c-414b-36f9-bb51-dcf2258c2ce9 | -11.96063 | -43.37474 | 2026-07-29 04:14:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99c1f352-d508-3bbf-8648-24c659303570 | -14.20487 | -43.97375 | 2026-07-29 04:14:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6cd231f-e21e-37ce-919c-028e3a130f9e | -9.13695 | -46.36018 | 2026-07-29 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c45a329-51bd-366f-bd86-f28682548a50 | -15.44066 | -41.37628 | 2026-07-29 04:14:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5050dbd5-d943-35a6-ab7f-0fdcafdf7863 | -11.52828 | -47.56071 | 2026-07-29 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0fba399-2b52-38ea-818e-07506dccdb60 | -13.56764 | -49.04679 | 2026-07-29 04:14:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a4ecc51e-f24a-39df-85f7-25546b05446f | -11.52911 | -47.55618 | 2026-07-29 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 385ff974-0b1c-3108-9416-60d47c06aac0 | -14.00911 | -53.9664 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dccb9698-3118-3ade-8866-f51a60bd0009 | -14.06804 | -53.98098 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1e3a386-d6a7-368a-b22e-f6e9da61a49f | -10.93205 | -43.06145 | 2026-07-29 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| d7c4ae22-9478-3e44-8911-aef0edfcdfed | -9.13632 | -46.36387 | 2026-07-29 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57f60563-6da8-3811-b77c-005ac74584d5 | -10.90429 | -45.21567 | 2026-07-29 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cec20c29-e5db-3cea-9574-3fee238a35c9 | -13.71206 | -51.91847 | 2026-07-29 04:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff6e5ae5-6513-32fc-886b-f3d49cf3b41e | -10.90509 | -45.21103 | 2026-07-29 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75c0a07b-4e30-354e-87c6-c2791c096d80 | -11.52499 | -47.55297 | 2026-07-29 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d9ed073-6127-3aa0-9a76-cc0c6620b6c8 | -13.15213 | -51.30249 | 2026-07-29 04:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43ed100c-b06d-3353-bbae-3cb6f6b5146c | -14.06552 | -53.97868 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d11a269-0452-38e7-a323-077d73e14552 | -14.01539 | -53.9677 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7936a635-8e6a-3679-a89f-f2c473d8c5ce | -15.43621 | -41.38295 | 2026-07-29 04:14:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| e4c52a9c-fdb8-3625-aa55-4a3cde031f2b | -14.72474 | -47.14865 | 2026-07-29 04:14:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a713296-81bc-3023-a462-7e0b1b61c0d0 | -14.19116 | -51.90332 | 2026-07-29 04:14:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f12ff784-de35-32ab-99d3-401aa8f07dfa | -14.00283 | -53.96508 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a747e17-4137-3147-83c8-5c6490d333ca | -13.3978 | -43.56776 | 2026-07-29 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e01ea850-aae0-3377-88d5-5b095eea9fd8 | -9.59791 | -49.30503 | 2026-07-29 04:14:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d89a1e09-57ee-3efc-8afd-ffe5ccc28544 | -14.02167 | -53.969 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1913d1a4-f5af-349d-ada0-730f55632fd9 | -14.03562 | -53.97916 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| de7234fa-dd00-37b4-a542-7f6ad64c446a | -14.23864 | -41.14545 | 2026-07-29 04:14:00 | NPP-375D | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a82f91cc-2b41-3ed7-940c-092979bac7d4 | -15.43955 | -41.3835 | 2026-07-29 04:14:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| fb4ed890-d49a-3c7e-af50-c422ef2f40c9 | -15.03665 | -42.25145 | 2026-07-29 04:14:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 805a6a5a-3e83-3880-a048-7a78ddac6fcd | -14.03832 | -53.9834 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| db329ef5-b4a5-31dd-82e2-13093140eae9 | -13.71513 | -51.91969 | 2026-07-29 04:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7b8c163-d118-321e-bd2d-3fe77647ad26 | -9.08146 | -50.58994 | 2026-07-29 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de561432-3cc9-3389-a1f8-d185f97ab93c | -8.96443 | -47.44823 | 2026-07-29 04:14:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de097229-455c-3e5e-842e-fa0dab9f5ffe | -14.83901 | -41.24595 | 2026-07-29 04:14:00 | NPP-375D | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ccb0cd3c-9a27-3a87-acf3-9c94ba4a7e9d | -14.19039 | -51.90706 | 2026-07-29 04:14:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21a036e7-4a12-33e6-b784-d2191020855e | -10.93672 | -43.05451 | 2026-07-29 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| d02ef93b-3d17-3797-8368-d85b1e014ac4 | -11.26594 | -49.56109 | 2026-07-29 04:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68484c4d-db72-31c4-8024-8efaeb2b008d | -9.09466 | -50.61171 | 2026-07-29 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecb8e77e-ee76-36b2-b8d3-70bf03dd0e34 | -14.06697 | -53.98594 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2833835-b35a-36a8-93d8-b056c4c93682 | -14.18963 | -51.91081 | 2026-07-29 04:14:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8ea156f-a0cd-3de3-ad59-9ce2d234677b | -14.0588 | -53.96294 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9bcff585-f0fb-35fd-987b-6924d9e8775c | -14.39307 | -48.02005 | 2026-07-29 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f737ad9-b2c2-3f8c-b796-f0728e179aed | -14.05258 | -53.9614 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90c8d0cf-d5f7-374d-9670-ba0ac1548414 | -10.35334 | -49.74805 | 2026-07-29 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b602c55b-f178-3f6c-bf90-a9371d37643d | -13.45408 | -44.04167 | 2026-07-29 04:14:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fd1ed92-9a6a-3fb9-bc47-82a825d9909e | -9.60744 | -47.76699 | 2026-07-29 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d9ad7990-2803-3349-8d36-d51775da9ac6 | -10.9333 | -43.05393 | 2026-07-29 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 57e86f34-286d-318b-9fca-52bef36f49f9 | -13.71131 | -51.92225 | 2026-07-29 04:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c9d7c7b-d11f-34e7-b298-e37e13e47b55 | -14.05515 | -53.96556 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9fa77b3-0480-3d6b-a0a6-dfa90cd4443d | -13.47973 | -44.03795 | 2026-07-29 04:14:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6bab8020-bb7a-324d-a721-03f9eb3c13a8 | -14.04891 | -53.9641 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2dfea8d8-bf17-3ca8-aea1-26a12f5e3809 | -8.44627 | -51.55272 | 2026-07-29 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 184c7da3-2e4a-333f-93a9-3deb79f616ae | -14.43784 | -44.86755 | 2026-07-29 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 374e7d18-b79b-391d-8f38-a23a02c29a9a | -15.06689 | -41.21606 | 2026-07-29 04:14:00 | NPP-375D | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| daa3fb7b-75e2-3372-8528-041e5e84eb15 | -10.93392 | -43.05017 | 2026-07-29 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| f590c548-59d1-3561-94db-788b2887d6ec | -14.20831 | -43.97436 | 2026-07-29 04:14:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a778739-33de-3318-bc23-f8f763e479ed | -11.18108 | -49.93488 | 2026-07-29 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8337b0f5-b15c-398d-b8e1-fcb90da77932 | -15.44735 | -41.37736 | 2026-07-29 04:14:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5616a1a4-ea87-3c71-8388-d71a415f150c | -15.87514 | -43.60114 | 2026-07-29 04:14:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6450d844-915e-3722-9dff-cd7c53022872 | -11.52775 | -47.56284 | 2026-07-29 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f48c9ac-0cdd-348d-8bb7-597983f58202 | -14.02684 | -53.97558 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93b7ecac-80fe-3000-b6e8-11d0028cb591 | -9.08701 | -50.59101 | 2026-07-29 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06580454-3dc4-37b0-890c-7d1797612155 | -14.73133 | -47.13499 | 2026-07-29 04:14:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df05a8f0-42f2-3d1e-bde9-99c608f056a7 | -10.32965 | -46.86867 | 2026-07-29 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5904b5bd-12d2-3354-b4d7-ea51d66b1b9f | -14.03451 | -53.98429 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README8.md)
