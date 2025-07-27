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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab9a9874-fd10-32f8-90e9-d188cc3dae6f | -8.172 | -43.20018 | 2025-07-27 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 04d20625-21b0-3641-b753-2ef3d3fa4204 | -12.71495 | -47.00132 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bed0c75-cff3-3139-8d05-7afed6ec3c09 | -12.00408 | -45.82855 | 2025-07-27 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66d08ae1-2fc5-3e1e-a6b3-2f3cb8c7c936 | -7.58207 | -41.77847 | 2025-07-27 04:08:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b4b62dc0-d955-3e11-b88c-945b1225692c | -13.09609 | -47.35884 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a36cb78b-457e-3610-8268-1b483d95cdfb | -11.965 | -46.71041 | 2025-07-27 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1daa29da-1549-3330-8eb5-49923cc169f7 | -8.82743 | -44.51233 | 2025-07-27 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 44d918a5-3a49-3a99-898b-38693f80ec04 | -12.693 | -47.01681 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ec4431d-0592-3e50-bcbf-10058dad2e31 | -12.04667 | -45.83591 | 2025-07-27 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ab14f56-5969-3bca-b887-c348d9142381 | -13.48927 | -45.50198 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| dad84850-6ef8-36bb-9014-0f1fecfebb58 | -7.37409 | -43.43086 | 2025-07-27 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f4ec630-f174-3735-a420-f6d4909b0d0a | -12.70579 | -47.00972 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 953b18f9-d196-3282-81f7-5297107960ec | -7.9194 | -43.09801 | 2025-07-27 04:08:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51976202-2682-3b6f-ac9f-017871c22022 | -13.132 | -47.3318 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be03112a-c924-3a8d-b98f-a1845b34155e | -13.13654 | -47.32812 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6569a75e-da75-35a2-a821-4e1fb9a9b19d | -9.66088 | -40.59269 | 2025-07-27 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af3a6330-8a4b-3d3c-a768-b9ef8c40ab5c | -7.58262 | -41.77501 | 2025-07-27 04:08:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 83b765a7-d641-36bc-9120-4d4085d2874f | -14.22085 | -43.96561 | 2025-07-27 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97cad37b-6800-32e9-ab84-0a6558754c3b | -9.12684 | -45.86659 | 2025-07-27 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce11b7c6-0b3a-33b1-92bd-fcacf90e763a | -13.08324 | -47.3429 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d45935c3-aa91-3419-93db-0f3cde783bef | -11.51178 | -46.87897 | 2025-07-27 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eea063e0-b628-3f41-b7a9-e7a1c13db2f5 | -12.7087 | -47.01518 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e6e5666b-0b47-373e-b7d5-2c2c22a24685 | -12.71122 | -47.00063 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f55b98b2-61c4-3154-90c1-3763f26b9bb2 | -12.1424 | -44.73191 | 2025-07-27 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcd1df32-a58c-33f8-9450-559eaeafab4d | -6.99336 | -47.08384 | 2025-07-27 04:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ce23e0b-b4bb-303b-9bcc-94ac06815f5e | -12.67809 | -47.01382 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b6de208-68de-3bde-bfba-84a475ecacd0 | -6.95355 | -50.45947 | 2025-07-27 04:08:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 418d9d43-c2dd-37e0-8a16-6f5f130e3653 | -9.43487 | -51.74655 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6faf45df-1efb-3a92-8394-9149eac1f419 | -9.81831 | -47.7559 | 2025-07-27 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73572211-dc2d-3ac0-9a45-4d1e4b0e9330 | -13.71756 | -45.67256 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8f5a7b2-4e78-318c-8f02-f2baa1a64d92 | -8.01202 | -48.17738 | 2025-07-27 04:08:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88ba4b8c-743e-3164-aa68-1a6061d7d26b | -13.09807 | -47.32502 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36ad5b01-fde0-343c-b3bb-9042a12c69fc | -12.7097 | -46.26816 | 2025-07-27 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78337182-ed53-3240-a42f-33730e44c815 | -13.10658 | -47.3209 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c285321-45e1-30b0-a6b0-f76c89f3c0cb | -12.70835 | -45.02629 | 2025-07-27 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9582d93-a0af-3c78-b682-e742aaeaf031 | -12.71037 | -47.0055 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3606389f-8a71-3cbe-a628-e2ee876110f3 | -8.51095 | -47.48886 | 2025-07-27 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87c3b814-56e6-341a-bae3-a3268e13dd84 | -9.3855 | -40.26509 | 2025-07-27 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6fb21ea6-f9ae-31f8-b0cb-c3ab8c1a9983 | -9.42954 | -51.74529 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d863757-f0e7-329b-95f3-8d7a7f877c1f | -10.59835 | -44.32169 | 2025-07-27 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a3a3394-cc04-36cd-9207-a1b339091c0a | -12.67972 | -47.00451 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c15d8b18-6810-3286-a7dc-17edd3cea387 | -9.43657 | -51.75033 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1dd0f92d-095d-3629-a578-21a016d896ca | -7.75414 | -51.1223 | 2025-07-27 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7840516-1641-351c-b0df-b872a45f91f5 | -13.53497 | -45.52593 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9276abd-3a0c-3437-ab7d-6cef0a4ecc61 | -7.20578 | -44.16922 | 2025-07-27 04:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5969c444-fb63-398e-90be-b9ecb40b41be | -11.30227 | -55.11826 | 2025-07-27 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da0333e0-e3f4-3f53-9d55-6cb62eb01f3f | -9.50863 | -40.375 | 2025-07-27 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d0de9e6e-6d49-31a0-91a6-5396b47a2e0c | -7.88941 | -42.47778 | 2025-07-27 04:08:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d0a39f7d-39a0-3922-8a41-1fe7b4370c8b | -14.22142 | -43.96205 | 2025-07-27 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3181df2b-1a20-3ad0-a420-bb79f565f964 | -10.83696 | -46.68992 | 2025-07-27 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92f00b73-1d7a-3580-9515-5ae11cd76aec | -8.8709 | -49.00695 | 2025-07-27 04:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9791fd4e-8aa0-3a5e-a7c8-6de848cb77dc | -8.17256 | -43.19662 | 2025-07-27 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0fa946b6-912a-31ae-b80f-71dbe9ef0e53 | -12.6893 | -47.01589 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d2a254f-f7c8-36f3-a515-39e3b9f81a42 | -13.12217 | -47.34355 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8642575b-6965-3edf-84bc-69354e2b21f4 | -9.4312 | -51.74931 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3bc58b01-222a-3323-8bd3-343cc4755fe4 | -12.68049 | -47.00016 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 524ba166-fd7c-3465-9356-da35d1a1c1db | -12.05022 | -45.83653 | 2025-07-27 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83272178-1b2c-3563-8736-653f3e73f99d | -13.12058 | -47.35275 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c68bcc90-333c-3451-972f-782dfa1aaacb | -12.67539 | -47.00231 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b05df58-7104-3b68-a485-e015739bae81 | -7.42431 | -44.7156 | 2025-07-27 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a18b9ed-e502-39db-ac49-5d2d2d70a0a4 | -10.62155 | -44.76196 | 2025-07-27 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fd3f034-edfb-33aa-9c34-77040c1141ff | -9.99777 | -44.36989 | 2025-07-27 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e34a391-9c58-3489-b153-2be639ef965e | -13.10577 | -47.32554 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71002323-09ff-3890-aadd-49900bc9259f | -7.38516 | -44.66906 | 2025-07-27 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e41019e-fa46-39ab-9f0b-7232de7f4be0 | -9.57625 | -43.87321 | 2025-07-27 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e3cbb35-52e1-32a6-a2f8-6200e1eee172 | -14.22256 | -43.95494 | 2025-07-27 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c203e09f-9d41-3856-807f-3b17642b9a6e | -7.37573 | -43.44229 | 2025-07-27 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc7fbefe-724e-3eb0-acae-d96b5388fa03 | -8.01343 | -48.16896 | 2025-07-27 04:08:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 928be91c-3456-310b-9428-64ea59c2117c | -12.71206 | -46.99576 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 93682aec-3e67-35af-b476-e6f542cc481e | -13.13122 | -47.33635 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b115085-7497-3bc8-8c6a-b281e5f4d8db | -8.29008 | -45.00768 | 2025-07-27 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6749a7b-325c-3113-8859-12afa1801d52 | -11.97322 | -46.70716 | 2025-07-27 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7f78821-0303-38c2-961c-936b6683e19d | -13.71475 | -45.66803 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c76adaed-88fc-318b-bef8-0526983218c0 | -12.71115 | -45.03064 | 2025-07-27 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1a7f06d-0973-3f39-a9a1-7a56099ab25b | -13.11422 | -47.36697 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c30c9e08-9e7e-3d07-b23f-62f2800aa4c5 | -8.86434 | -49.04382 | 2025-07-27 04:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60bf7f99-7492-3503-8880-15a203af4094 | -8.29364 | -45.00828 | 2025-07-27 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64bba1cf-5e8a-343e-9eea-bf9665c11323 | -12.68559 | -47.01507 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d4f6a19-a53e-3070-b644-4a8ea54d38d8 | -9.4319 | -51.74561 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dcdc9a16-2140-3164-a316-ed73d710dc88 | -10.00838 | -48.22597 | 2025-07-27 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ab1c936-218d-3a95-8388-e6b8636765e6 | -13.11802 | -47.36763 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 893ccf8a-7f0d-3e44-abe6-cbb7e522f3ec | -9.57742 | -43.86592 | 2025-07-27 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fb4d2973-24d6-32c7-bf22-c7617b30eb8e | -13.12376 | -47.33434 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e851782b-3476-3e27-b1ab-763136878c10 | -12.68476 | -47.0198 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a577e465-9883-3738-9fed-5b9e3e7cb511 | -9.81765 | -47.75964 | 2025-07-27 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be45278e-1490-3e7e-8c9d-d8d63b77bb36 | -9.43046 | -51.75325 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fef62b1-5135-3900-b13f-d315cd1029df | -9.42973 | -51.7571 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7d90e73-04d6-3e1c-b31f-62c158bb0c5d | -9.56107 | -40.64946 | 2025-07-27 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7f8facdc-682c-314b-9d8b-64036868be8c | -12.67728 | -47.01845 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95197013-5d43-3556-8aae-f83d6e17d8e9 | -8.29075 | -45.00362 | 2025-07-27 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fa27dbe-878a-3e06-b636-104295169f28 | -6.9541 | -50.4563 | 2025-07-27 04:08:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 70b2aee2-1772-3f54-a5bf-6045ca737357 | -13.49271 | -45.50261 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7bd3c4ae-3a09-3ee1-9ce7-e1419d39da2b | -7.37515 | -43.44592 | 2025-07-27 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d324dce1-d9d0-3631-a085-d4d91599c78b | -13.72037 | -45.67707 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c43a343-da1e-3645-9580-d7d320fe5886 | -9.42887 | -51.749 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c35a54bf-adf0-3355-aa83-b62efe2a46dd | -7.1011 | -44.87579 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8b3c78b-9e26-338e-a038-3458783127bc | -7.08789 | -44.91129 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d30cbfc-20e6-3004-af3d-d959c6121b02 | -12.00339 | -45.83265 | 2025-07-27 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44c37886-0afd-3783-b6f8-1288e4139f9c | -9.57346 | -43.86904 | 2025-07-27 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e45ee676-7441-3f88-80e6-23c994224360 | -7.53204 | -42.41705 | 2025-07-27 04:08:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README11.md)
