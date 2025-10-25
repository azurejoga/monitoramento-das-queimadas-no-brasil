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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efed8868-96b9-32e0-a221-275c341d7040 | -21.05007 | -47.33116 | 2025-10-25 04:02:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4d64839-0947-3792-8e3d-5697f386646e | -16.94715 | -44.48338 | 2025-10-25 04:02:00 | NPP-375D | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36d01842-366b-3ff9-a411-2ccbb652062f | -21.20597 | -46.71852 | 2025-10-25 04:02:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e6a00970-ba2d-3a2f-8c64-77f196f03275 | -18.55743 | -50.2752 | 2025-10-25 04:02:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 28a45fb6-c23f-31e1-bd0f-7988f6812221 | -16.58798 | -43.50165 | 2025-10-25 04:02:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| bc0f0198-4aed-3c1b-9485-9fce9eba9532 | -21.09906 | -49.24989 | 2025-10-25 04:02:00 | NPP-375D | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 15a25398-1a14-3c29-a136-9ac9804adf84 | -15.5346 | -45.70272 | 2025-10-25 04:02:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b58902d-e16e-3855-ab46-ddaf06f37a02 | -18.92867 | -42.69854 | 2025-10-25 04:02:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c88d5437-607e-307c-b346-0c3975bfcb62 | -17.38144 | -45.50042 | 2025-10-25 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bcefce47-67b0-3e54-afce-d5ce37cd8cbc | -21.07016 | -43.63518 | 2025-10-25 04:02:00 | NPP-375D | SENHORA DOS REMÉDIOS | MINAS GERAIS | Brasil | 3166204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 68adebf3-6c71-3007-ab1f-037179141e9c | -21.36998 | -45.03071 | 2025-10-25 04:02:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 56221464-6aba-3318-a806-4a9c57eea51b | -18.55747 | -50.28143 | 2025-10-25 04:02:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c6f87f8e-1e11-3deb-b0fd-5b3b2d28621a | -14.90174 | -52.46092 | 2025-10-25 04:02:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7ed8cd3-5848-3ae8-a8d0-5e7bf0cdfaaa | -16.2189 | -46.47763 | 2025-10-25 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa11ee4d-d723-3594-a7b4-cbb78e2e324a | -20.10993 | -45.84837 | 2025-10-25 04:02:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62dda536-2675-3940-84f9-0cc58439a708 | -21.92171 | -46.50465 | 2025-10-25 04:02:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8e8f5fd4-a1f6-3d04-a60e-cb5938bf5630 | -21.04933 | -47.33506 | 2025-10-25 04:02:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 458f8b6c-78ae-37c3-9600-b1417d1843e3 | -15.5292 | -45.70839 | 2025-10-25 04:02:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1070984-6d25-36ea-8e1c-02a576147ca4 | -21.15517 | -48.5168 | 2025-10-25 04:02:00 | NPP-375D | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3d4918ea-6ca1-3497-a447-777dc60084a7 | -17.47263 | -45.99042 | 2025-10-25 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ae76f95-a217-318c-bfab-2affadc82b60 | -21.20209 | -46.71761 | 2025-10-25 04:02:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 933eb483-34c1-3e05-b22b-8c8ac3f3f955 | -18.56959 | -50.27464 | 2025-10-25 04:02:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 3bb35b88-6a6a-3c49-bdae-54e57348154a | -22.58058 | -42.05019 | 2025-10-25 04:02:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a1e65461-3f6e-3207-adf1-999395a69c20 | -20.43573 | -46.58582 | 2025-10-25 04:02:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ac1fae5-5603-392d-80f3-4d30cd05c42d | -14.38309 | -51.53141 | 2025-10-25 04:02:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d87ade11-602f-3f86-9c20-4b49efd8c200 | -21.918 | -46.52443 | 2025-10-25 04:02:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 3fafce3e-7075-3c95-a6c3-844f854d3a36 | -20.45526 | -45.26569 | 2025-10-25 04:02:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fe9475e0-502e-39b9-bb41-0616dd53b5a4 | -21.49972 | -44.26298 | 2025-10-25 04:02:00 | NPP-375D | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 31cc3ec2-58f9-339d-b3ec-62da4d9fc279 | -15.22287 | -47.93005 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6894d092-7087-3a71-845b-b3353a207501 | -15.2369 | -47.93289 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9c24bd75-8261-374a-8824-8ac7c2c45ded | -18.55235 | -50.28032 | 2025-10-25 04:02:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 295db3ab-4905-319f-b52f-97962c0293c2 | -15.23564 | -47.93072 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0b6c5e87-e254-313f-a710-1d568fafb731 | -14.88642 | -52.44085 | 2025-10-25 04:02:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e461cf1-ed44-3caf-8565-4a2d8859ec2b | -18.55812 | -50.27832 | 2025-10-25 04:02:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| dd5803ef-03f8-3712-a930-db6216f8d1d4 | -15.3127 | -48.07323 | 2025-10-25 04:02:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9d4ab20-f336-3ee7-bb32-a1de6730bc98 | -18.16638 | -51.76147 | 2025-10-25 04:02:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 28b12391-dba3-37ee-9623-1add911ce535 | -18.05338 | -42.53662 | 2025-10-25 04:02:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fbf3058e-74b2-3f79-a695-8f1d45f4bd91 | -17.37845 | -45.49475 | 2025-10-25 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aac14e53-b565-3fb9-9607-28f20ee0bf00 | -18.55617 | -50.28136 | 2025-10-25 04:02:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 772b6f69-a244-3ec8-8213-dcfa8b3aed89 | -18.55681 | -50.27824 | 2025-10-25 04:02:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| fbd47d33-e591-3cfc-b1bb-7872edd6d6e5 | -17.55132 | -43.79118 | 2025-10-25 04:02:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0dd1dcad-e9fd-3305-a052-bdc3910a8b43 | -18.78898 | -48.03868 | 2025-10-25 04:02:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 71984d1f-d983-35e8-bde3-3de974a2de9a | -17.41427 | -46.88461 | 2025-10-25 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d0f0bd3-0f7f-36ef-b27a-a667bf6ec762 | -15.76662 | -46.10313 | 2025-10-25 04:02:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d538f14f-e480-3a01-9007-61a743ba5ddd | -19.76651 | -48.29823 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 92d862bd-f4e4-350e-9df1-3bf0cd0db093 | -14.38809 | -51.53727 | 2025-10-25 04:02:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d80df00a-0edf-3eaa-ba51-c4e2ee1d6be1 | -20.82714 | -45.00422 | 2025-10-25 04:02:00 | NPP-375D | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e622217b-f623-37f4-b43d-8315b9045020 | -15.23218 | -47.93216 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 479b0c2d-156c-32a9-8ab7-68e76d0052bf | -17.21336 | -47.65561 | 2025-10-25 04:02:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8879e571-9d78-31b1-a473-a11eb07e65a9 | -19.31795 | -42.2877 | 2025-10-25 04:02:00 | NPP-375D | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 80432c7e-f2ef-3f22-beac-e7671ef4b394 | -18.56896 | -50.27768 | 2025-10-25 04:02:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| d8e017e0-b835-3841-802a-99aed4383156 | -15.23092 | -47.92999 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c57b73cb-8de8-3ebf-8107-46a05e110df4 | -16.21817 | -46.48161 | 2025-10-25 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ebe66d3-698f-32c5-a866-25fa54191234 | -21.92752 | -46.51595 | 2025-10-25 04:02:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| ff31eb9a-d146-38fa-9b34-2e89b0ab93b4 | -16.26463 | -43.61793 | 2025-10-25 04:02:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f02c41f-73e6-374f-9e87-e15c09382a6c | -21.88957 | -45.26823 | 2025-10-25 04:02:00 | NPP-375D | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 10c5675c-7f91-3dfd-ab92-2a75d578494b | -17.41922 | -46.88151 | 2025-10-25 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 050378d7-ea77-3d3d-8d74-7d247f6dca14 | -16.09794 | -46.74858 | 2025-10-25 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50e64f19-6cb9-36ec-adc3-e5218c266fe7 | -19.874 | -46.97935 | 2025-10-25 04:02:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46db55b7-8ff3-3c8a-851c-220ae253505c | -15.30693 | -48.07761 | 2025-10-25 04:02:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1364e5cd-b891-3d89-a5ef-e24b8284ed63 | -18.054 | -42.53288 | 2025-10-25 04:02:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f582d371-9269-33f1-9d83-24f799e66fe3 | -18.16258 | -51.75174 | 2025-10-25 04:02:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9350c86a-f993-3433-9bfd-34b812367bbb | -15.53053 | -45.70118 | 2025-10-25 04:02:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c840dfb-5109-33bd-9649-91af21774b84 | -17.37457 | -45.49408 | 2025-10-25 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ff6b128-9648-3d92-b46b-d920f332ab29 | -15.22031 | -47.91831 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4382472e-8942-3c18-807b-472baaac3328 | -16.58444 | -43.50101 | 2025-10-25 04:02:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6298bc2c-e665-33bc-9e45-345c41f18389 | -18.80221 | -44.81267 | 2025-10-25 04:02:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd13bd74-101e-3590-833b-7cdab232569d | -18.17197 | -51.763 | 2025-10-25 04:02:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fa3002dc-c6a6-363a-96e0-c24e33432295 | -15.24051 | -47.93929 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a8ceb5e-9a85-3d68-8957-d6c08feb0182 | -19.84865 | -49.06977 | 2025-10-25 04:02:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49a4bdab-3314-3445-b382-d3e140f9565b | -20.44058 | -46.58163 | 2025-10-25 04:02:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64457aba-3498-3650-84ff-ee04ed5c4d32 | -19.75955 | -48.28696 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5dc08a1b-90d1-34ad-bead-f375330764c0 | -15.22853 | -47.92599 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 962bc196-cc64-30c6-9c83-23ccf5832da2 | -19.33307 | -49.09188 | 2025-10-25 04:02:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 504f228a-248c-34b1-b06e-4915407319a4 | -15.47174 | -50.46885 | 2025-10-25 04:02:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddbf1083-3b88-347e-a65e-85caa65c23b6 | -16.36319 | -49.9352 | 2025-10-25 04:02:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 203298d1-3c5a-39bc-9a16-e0a391365fde | -19.95356 | -41.7241 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a777c587-e177-3d52-a7a2-8ba99c5e4612 | -17.06015 | -48.03762 | 2025-10-25 04:02:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe30dd5e-21b8-32ef-8f92-fd4bb00f955f | -14.91012 | -52.45235 | 2025-10-25 04:02:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fa8af48-112d-3a80-ab85-6532b791621c | -14.56064 | -54.18496 | 2025-10-25 04:02:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98f3e820-7528-3396-b683-161c6cb63927 | -18.17285 | -51.75894 | 2025-10-25 04:02:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5db66b0a-804a-32f6-bf9d-cfd200a7682c | -16.0937 | -46.74762 | 2025-10-25 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96790b7d-f4a7-3c09-ae59-b207574d3f29 | -17.20895 | -47.65459 | 2025-10-25 04:02:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de640fcd-a2ce-3130-baf8-88c5f74246a0 | -15.53589 | -45.69479 | 2025-10-25 04:02:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b705a191-1154-3962-b400-71921b6941b0 | -14.9112 | -52.44727 | 2025-10-25 04:02:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 818c1450-9e91-3baa-8c35-00f919acd49a | -16.94461 | -44.48502 | 2025-10-25 04:02:00 | NPP-375D | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcac8d89-1fe1-3849-8035-5ce5e60208e0 | -14.40287 | -51.52641 | 2025-10-25 04:02:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3b8151c3-e080-3816-ad8d-b438a22ebaae | -14.89263 | -52.44237 | 2025-10-25 04:02:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19e668f6-f477-397c-86cd-a2f1a6d7f063 | -14.89153 | -52.44749 | 2025-10-25 04:02:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0da023f1-6e49-3b12-9d8b-52a60ccd332f | -21.92276 | -46.52016 | 2025-10-25 04:02:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 1a74c02a-fa23-38e6-9109-e42dfc1b992f | -18.63635 | -43.06691 | 2025-10-25 04:02:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 91495fea-79bb-3397-ba3b-c71fdc9d8a7e | -17.37546 | -45.48913 | 2025-10-25 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a429ccfc-ccce-3249-bef6-502306e82324 | -19.33188 | -49.08979 | 2025-10-25 04:02:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d3d52635-0ffc-3558-a6cf-f8ddc051691b | -18.36934 | -43.65703 | 2025-10-25 04:02:00 | NPP-375D | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 537d0e6f-ba5e-36e6-b154-fb9962ce030e | -20.40049 | -42.89224 | 2025-10-25 04:02:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2afdacea-3926-3e84-a37d-7d7e2723673e | -21.05339 | -47.33587 | 2025-10-25 04:02:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9304f798-7bfe-3a68-bb92-557e975697ef | -19.3219 | -42.28461 | 2025-10-25 04:02:00 | NPP-375D | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0380fba2-53ba-360f-911d-3937de50f3c1 | -20.38691 | -45.91854 | 2025-10-25 04:02:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 218990fe-1d66-3b6f-abe1-d466d4240cb1 | -15.24154 | -47.93402 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d8ca6e7b-808e-3619-bed2-d3efd4fe542c | -18.28852 | -42.86765 | 2025-10-25 04:02:00 | NPP-375D | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README25.md)
