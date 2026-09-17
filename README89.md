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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e62685f-1797-3e7e-a987-e730d9fb96d6 | -9.8517 | -46.9269 | 2026-09-17 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 390762e2-31d8-3705-974f-61d1e8366ece | -9.8697 | -48.3595 | 2026-09-17 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 84a95f92-cb06-3967-af7b-5941d9a9df75 | -9.7687 | -46.1067 | 2026-09-17 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 1ee3ce0d-69d7-3bad-a4f8-c1b623ed3937 | -7.841 | -44.8614 | 2026-09-17 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 7b1639b3-8908-31c6-a907-859e4058a11e | -11.3467 | -47.2361 | 2026-09-17 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| dda76cff-eb3e-348e-8327-c8bd621e1471 | -12.3571 | -50.842 | 2026-09-17 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 044cddb1-dee8-3042-99a7-c392fb7992cd | -18.8906 | -46.8284 | 2026-09-17 13:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 87eaf43f-5f02-31ed-ae70-00bc8f1195ed | -12.3578 | -50.7991 | 2026-09-17 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 79e2810b-5b17-3a19-9157-aa31d995093d | -9.8884 | -48.3794 | 2026-09-17 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 30f56b10-d857-3544-b0fa-7e190560d72f | -3.2212 | -53.9422 | 2026-09-17 13:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 156.2 |
| 46467bcb-2131-3803-a124-a9de4da7d8c4 | -9.8694 | -48.3814 | 2026-09-17 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 0304c7da-0204-3448-995b-029549f716ea | -6.9896 | -43.6514 | 2026-09-17 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| bd905782-65f8-3c7e-92f6-996650976410 | -10.8118 | -46.1594 | 2026-09-17 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| bd2d9797-9541-3390-8b81-d6d39fecb608 | -12.5094 | -50.8664 | 2026-09-17 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 385.3 |
| 5aea8649-9cd6-3df9-b4f0-98bac49501e4 | -10.8919 | -54.0062 | 2026-09-17 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| f4a567ba-d121-396c-8950-009aa49ef789 | -12.3085 | -47.9539 | 2026-09-17 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| d827a2a3-f851-3317-a73a-93b6f9081b6f | -9.8319 | -48.3636 | 2026-09-17 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| ee5b6c58-58f4-3a21-a7d6-04e9f9f217d1 | -6.7851 | -45.2308 | 2026-09-17 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| be81278d-b231-3f1b-986c-456ae1c3f5ce | -12.3387 | -50.8014 | 2026-09-17 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 36eaf9ca-7cb4-3759-8da7-d39ca59e0f0a | -8.8647 | -45.8693 | 2026-09-17 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 5fdddb80-8481-3fa5-b455-42f172b4c8b7 | -8.75141 | -66.56219 | 2026-09-17 13:25:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ebdd4c13-015a-33c9-a0c4-a6c61422cdf2 | -8.74894 | -66.58118 | 2026-09-17 13:25:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 17a3eac8-5955-3c40-9c2d-c0559955d411 | -9.41626 | -66.16051 | 2026-09-17 13:25:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d67d6d31-cf69-3310-a83c-d0bdc4837015 | -8.75039 | -66.58793 | 2026-09-17 13:25:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 7a7b6fb5-fb04-3353-be15-a5b3d7b73732 | -8.75271 | -66.56892 | 2026-09-17 13:25:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 16e2ee7c-2e7e-3680-8fe0-caf0517b34bb | -12.6638 | -50.762 | 2026-09-17 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 2f7ef780-7b6d-3292-a08f-eff4d45383bd | -9.5512 | -45.4296 | 2026-09-17 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 1a050e5e-1e06-3647-a9e4-83d77147f9d3 | -7.8033 | -44.8651 | 2026-09-17 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 4ea99d29-2f24-35f6-815c-01f577e8285e | -8.4982 | -57.6468 | 2026-09-17 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 09ab5c3f-67a4-36fe-8bf7-e2d2738a068f | -14.1547 | -45.1442 | 2026-09-17 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 955d8764-d0e2-3b46-9945-c46b470e50da | -7.0451 | -42.0666 | 2026-09-17 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 102.0 |
| 6aaccf3e-ee88-3b5a-a18f-df62c1157029 | -8.5239 | -44.5153 | 2026-09-17 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 76092435-852f-3e3d-beac-a8ef577d472d | -3.2212 | -53.9422 | 2026-09-17 13:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 166.7 |
| 4e9db952-849e-3a84-a52c-e8d0b2ea931c | -13.6143 | -46.9561 | 2026-09-17 13:30:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 667dfd4f-0937-3de7-9675-0b2867e6ed30 | -13.6531 | -45.97 | 2026-09-17 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| bab52135-37e7-3e92-9536-d53cfae39d84 | -12.7051 | -48.276 | 2026-09-17 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| fd84d36d-7edf-30e3-ab39-e9a14b9fcd02 | -7.3669 | -38.9584 | 2026-09-17 13:30:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 135.8 |
| 488469f6-efff-36a5-a514-b05fb2af2622 | -12.4903 | -50.8687 | 2026-09-17 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 9781d70f-8bb2-3ce1-afa6-fd265d8fea27 | -9.852 | -46.9046 | 2026-09-17 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 8f8824a9-3d47-384a-84a8-27951ab05584 | -9.8319 | -48.3636 | 2026-09-17 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| ac344000-a507-31c2-9478-a9f886892783 | -9.7497 | -46.1089 | 2026-09-17 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 9145717c-4c77-3431-81ca-7253570df654 | -9.9143 | -46.5172 | 2026-09-17 13:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 159.2 |
| ff47753c-2882-359e-834c-bca2beb23641 | -11.8069 | -58.1759 | 2026-09-17 13:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 8f2ba459-66f1-3924-9574-04a0508c13eb | -12.5097 | -50.845 | 2026-09-17 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8cdfa3ce-4671-3b04-8f99-b2408965391e | -14.1552 | -45.1208 | 2026-09-17 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 07dabed3-c0fe-3369-907d-a4d8cdd22765 | -12.6816 | -50.8455 | 2026-09-17 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| e76d4c6b-2efa-3d21-962f-f9fd614e205c | -9.8884 | -48.3794 | 2026-09-17 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| a90a5a4d-40c7-3356-b657-0b78e44479bd | -7.6402 | -44.3303 | 2026-09-17 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 203.9 |
| ec86188b-4473-3e5c-adfd-6bf79d249e0d | -7.0349 | -44.6625 | 2026-09-17 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| d95132ed-c7ab-399f-be0a-8ff2c645d8da | -10.8308 | -46.1569 | 2026-09-17 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 851ed055-19e3-374f-8456-ade66fdc6ea2 | -9.8697 | -48.3595 | 2026-09-17 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 23b2c3f8-b3b4-3500-ae56-cbb5f4354b5f | -12.5094 | -50.8664 | 2026-09-17 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 9f8b86ce-c025-3be3-81b9-979c647b5da4 | -12.6635 | -50.7835 | 2026-09-17 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 20efde47-316b-3d53-9955-24773dff7a84 | -9.8694 | -48.3814 | 2026-09-17 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| bce2a93f-175f-3318-acb1-8c19b94a9bdd | -10.8919 | -54.0062 | 2026-09-17 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| fb564168-7cbc-32ad-b542-717402b90608 | -8.8647 | -45.8693 | 2026-09-17 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 337.9 |
| d6572ecd-aea0-3f14-804d-e8db348a39f7 | -12.5289 | -50.8427 | 2026-09-17 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 7fae6b2a-5129-340b-9dd6-bb0573e08a4d | -8.8644 | -45.8919 | 2026-09-17 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 84d3d359-ab4a-3603-8ddb-61db8d4d6be9 | -7.0164 | -44.6413 | 2026-09-17 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 169.5 |
| b1fdd024-aa74-3a22-9627-0e44288059bf | -8.8692 | -46.9882 | 2026-09-17 13:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 8da97da2-faf2-3856-bf54-68ec74570cf0 | -8.8459 | -45.8713 | 2026-09-17 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| ba39fb07-38c2-34bf-acf1-20b2376da35c | -12.49 | -50.8901 | 2026-09-17 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| c19edbb9-1d0c-3aa1-882b-7265b39f6373 | -10.9107 | -54.0045 | 2026-09-17 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 97350caa-c0e7-3b78-bcf6-8a9e304bcedc | -11.3463 | -47.2585 | 2026-09-17 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 140.2 |
| cff9ab45-c099-32fe-9c31-1ad94e66bc60 | -12.7894 | -51.2807 | 2026-09-17 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| e5eb483e-fa1e-330a-b9a5-dc3f63d21422 | -9.3943 | -50.1761 | 2026-09-17 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 29543bbf-bf42-345f-8e4c-40101838c254 | -9.3755 | -50.1779 | 2026-09-17 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 7c47680c-3822-3bea-9cf5-842a146e9073 | -7.7568 | -47.2927 | 2026-09-17 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 2f3f47a7-5b92-337a-afb4-86845456fd00 | -15.5012 | -53.7921 | 2026-09-17 13:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| aaa36cfe-cd1d-361a-89f8-a3f17823c6f0 | -8.8836 | -45.8672 | 2026-09-17 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 951631dd-6e1f-304d-8d69-ad4488194f86 | -7.0084 | -43.6497 | 2026-09-17 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 5244f7f2-63a4-3412-92f2-8bbd4aa7da63 | -6.9896 | -43.6514 | 2026-09-17 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 3ac387fc-6344-3d3a-8c8e-65fcb6cf4137 | -18.8906 | -46.8284 | 2026-09-17 13:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b31305e5-c125-3c35-8839-9c120289df14 | -14.1742 | -45.1407 | 2026-09-17 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 518f4384-b394-3c54-893e-2a18838fdb8f | -11.3467 | -47.2361 | 2026-09-17 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 4e897cf5-0490-377c-9250-34d373da2c9c | -12.3085 | -47.9539 | 2026-09-17 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| f3ab6cd7-ee02-35b4-96c2-41f69e483bfd | -9.3758 | -50.1565 | 2026-09-17 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 3351a9eb-c958-3bf2-a3a7-b16f858e0ca5 | -8.4796 | -57.6478 | 2026-09-17 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 503cf49c-2232-35c2-b7c8-7e8c3792faee | -10.8118 | -46.1594 | 2026-09-17 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 1ee1397e-1863-3bb1-9387-918abc073a20 | -7.8221 | -44.8632 | 2026-09-17 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 138.0 |
| dc0cf238-3fa0-312c-b1c5-867a05992a84 | -12.5094 | -50.8664 | 2026-09-17 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 39a51fc2-c87d-308c-918c-b58da9fde912 | -10.8114 | -46.182 | 2026-09-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 863012ba-1d7b-30bc-892b-742de1dcab4f | -9.8697 | -48.3595 | 2026-09-17 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| c3bdca61-c1f9-3fd7-afe6-5b9da162f6f2 | -8.4982 | -57.6468 | 2026-09-17 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 9c6bbea1-f945-37ee-b876-144d0565be1c | -13.6531 | -45.97 | 2026-09-17 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 317.2 |
| 06feb4bd-fbab-3926-9b3b-ff1f1392794d | -9.8884 | -48.3794 | 2026-09-17 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| f4e1b3ac-5160-3cba-af64-6285ba02f6a0 | -10.8308 | -46.1569 | 2026-09-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| be668447-5353-301d-9775-e744fa72bfdb | -10.7923 | -46.1845 | 2026-09-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 3131f8d6-4595-312f-8fe8-35bf0d62ffb8 | -13.6526 | -45.993 | 2026-09-17 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| cfa679a1-4bfa-3960-a67f-9aaf8e7b82fb | -12.5289 | -50.8427 | 2026-09-17 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 63414a50-7488-369a-9f96-37a9ac1ab7fc | -7.0164 | -44.6413 | 2026-09-17 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| e004b44c-b834-3a30-9477-4237740a24c7 | -6.9896 | -43.6514 | 2026-09-17 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 74ad53ed-1473-38fd-a614-87defdf445ab | -11.3467 | -47.2361 | 2026-09-17 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 87e26610-be4c-362c-965d-ea1068d932f8 | -14.5709 | -46.5941 | 2026-09-17 13:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 101.6 |
| cd13cf61-16d9-309a-827d-3e13ef503ae0 | -12.7243 | -48.2734 | 2026-09-17 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 2950b72f-b6ff-39f5-aeea-e9466735235e | -8.4796 | -57.6478 | 2026-09-17 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| c2c4e7a9-1cb0-37d3-806d-563012acc9be | -7.3669 | -38.9584 | 2026-09-17 13:40:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 179.8 |
| eb98a399-5071-366f-9157-a82eb078faa4 | -9.8694 | -48.3814 | 2026-09-17 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| a261b8d5-0ee2-3110-b036-5ad3dca4f282 | -12.7051 | -48.276 | 2026-09-17 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| c56c1218-d897-39ec-b5ff-d2db93230adb | -7.6402 | -44.3303 | 2026-09-17 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |


[Clique aqui para ver as próximas entradas](README90.md)
