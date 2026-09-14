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
| 9b5c556a-7a09-3ca7-8b71-220d8c542a00 | -13.43944 | -43.83176 | 2026-09-14 15:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| f848aed8-2664-30e8-8470-e227e2a2e0f0 | -14.48177 | -41.3748 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 36078f96-4f88-3856-91f7-b72af4168b9e | -10.79639 | -46.24956 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 785c4c6b-a449-30b3-a8c2-50cd74b60bc3 | -15.20359 | -41.53297 | 2026-09-14 15:46:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 2f8b8908-a516-3714-8e13-08e88c91186a | -11.08766 | -40.07771 | 2026-09-14 15:46:00 | NOAA-20 | PONTO NOVO | BAHIA | Brasil | 2925253 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 4dbc1213-06cb-3e91-9aca-b7e4550ce05b | -11.23707 | -41.03558 | 2026-09-14 15:46:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f99fd650-5229-3e06-99d3-cd59dd5e3e0b | -12.37908 | -42.40883 | 2026-09-14 15:46:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 79930fdf-ebf7-3877-a08b-7d10b6bbe757 | -12.70105 | -44.84963 | 2026-09-14 15:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3ca9b144-85aa-361d-86f3-7375c9eda98e | -12.13044 | -44.20529 | 2026-09-14 15:46:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 5f47f85a-db6e-3fe8-a1a0-dd8e14edca26 | -12.74685 | -40.42478 | 2026-09-14 15:46:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fe7a3f0c-a036-359f-8963-0958838afe7e | -10.79214 | -46.24036 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 5cd2b0ca-8b5a-3c3e-b35c-d64c6d4c359e | -12.97587 | -40.72176 | 2026-09-14 15:46:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6a2a3593-74b3-3eb6-9ec8-2122c17807cc | -10.83793 | -43.85486 | 2026-09-14 15:46:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9140f518-b221-3daa-991e-6a102dab2298 | -11.37209 | -43.96153 | 2026-09-14 15:46:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 21240de9-64ef-3cb1-ae5a-dbe36f515475 | -11.2268 | -43.45231 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1d13882c-0f19-3451-84b2-84c60520898f | -13.10112 | -42.38196 | 2026-09-14 15:46:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| aa5f77ab-a936-389d-9037-1aebd65144b4 | -11.50811 | -45.76706 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 6ef12bff-3a40-3b74-a1bf-e4d79b4c073c | -11.3802 | -43.95129 | 2026-09-14 15:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 4d145ff9-1581-3bf6-8e1c-5ec54fafcc99 | -11.18224 | -42.80964 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| a871747a-a608-38ff-a1cb-37cd7f9c04eb | -12.97128 | -39.8559 | 2026-09-14 15:46:00 | NOAA-20 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a2c6c219-ec2b-3628-aad9-90179705cc63 | -15.99756 | -40.68548 | 2026-09-14 15:46:00 | NOAA-20 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 164ed315-e10f-36fd-a53a-a85bc02ddbdd | -17.26201 | -41.5156 | 2026-09-14 15:46:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 6a89f888-c87a-3fb6-8f07-c99587cf19aa | -14.48088 | -41.37411 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 017be1dc-635f-3df5-9a9a-e96318c0c33b | -14.2689 | -44.78495 | 2026-09-14 15:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fe59dfde-5ccb-33a3-b0f6-dc87bc8ce765 | -14.26009 | -40.76484 | 2026-09-14 15:46:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 697a710b-8108-3dfa-8ece-7b5edc1c0f0f | -11.36634 | -43.96732 | 2026-09-14 15:46:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a6670fe7-0d11-3d02-9cc4-f28b3115287e | -14.6254 | -40.74039 | 2026-09-14 15:46:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| be408c97-a0c2-3f07-adea-50df346824cb | -10.04386 | -39.66141 | 2026-09-14 15:46:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 32.6 |
| a5b11abd-13e7-3708-b027-aaddf4785574 | -10.55115 | -46.28368 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bed3ee79-71b7-3486-b8c1-2b707cfb7251 | -13.43828 | -43.8211 | 2026-09-14 15:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 8b89665b-4dc7-3fb7-b84d-c2c78242e0ff | -12.95962 | -42.43245 | 2026-09-14 15:46:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d3c1453c-7337-3b0a-a453-1757fba6af44 | -10.30294 | -45.30223 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e62683c3-2f91-3093-8cf9-e1ddc58fd45c | -11.24526 | -43.44728 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 4eda7645-f9c1-376e-a616-3de607bf79da | -12.17673 | -40.38628 | 2026-09-14 15:46:00 | NOAA-20 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 24416be0-f217-3f4b-a132-4eca51099eb4 | -16.00435 | -40.68235 | 2026-09-14 15:46:00 | NOAA-20 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 7e373dea-3fa5-3d9f-b01a-ddb145a69361 | -14.33133 | -40.15707 | 2026-09-14 15:46:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c3fe21b4-f999-3086-bba6-d91a21237bc9 | -14.34914 | -41.43879 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 8ae59da1-5695-318f-aec3-d5904e69dd6e | -13.56711 | -40.62615 | 2026-09-14 15:46:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 98.5 |
| c81fc4b4-eed6-3bf1-bf2d-e7de278a8d28 | -12.23124 | -40.69991 | 2026-09-14 15:46:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 539e4020-b1d9-328e-b344-3db247e12de6 | -11.91766 | -39.18383 | 2026-09-14 15:46:00 | NOAA-20 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 36f0517a-a0f9-3754-b566-cf42f2fd05c4 | -10.80317 | -40.84318 | 2026-09-14 15:46:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 60d97ea6-6e31-3b9f-b621-34066981a4cd | -15.09562 | -41.26513 | 2026-09-14 15:46:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| d95518fd-3aa0-33be-8118-625cfe31265d | -14.08362 | -41.41933 | 2026-09-14 15:46:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| e4433f45-58d8-3b18-8024-1307389122e9 | -10.80901 | -46.2606 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 7f5c0020-5afc-3a66-b497-78801cfabf21 | -12.39394 | -44.39034 | 2026-09-14 15:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a0984fa2-10da-3827-a014-0dcf1d171de3 | -13.56804 | -40.63414 | 2026-09-14 15:46:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 75.8 |
| e92b9e5f-9a44-3fb5-9f43-e8ccf2c776c8 | -10.65787 | -40.33746 | 2026-09-14 15:46:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| ac138e4d-fdef-3579-926c-25b3fad596a1 | -14.27573 | -44.78397 | 2026-09-14 15:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0a2bf01d-2b86-3487-b806-165f46ef618d | -12.88745 | -40.42268 | 2026-09-14 15:46:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 97372dbd-32dc-3b6e-9bd3-f715a1c5ef8e | -10.31802 | -45.29041 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| b63f53df-c60d-34a6-a658-656a1c7df8ac | -10.6513 | -41.4738 | 2026-09-14 15:46:00 | NOAA-20 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b551550b-a7b7-37e1-98d1-e75c589f3104 | -11.18034 | -40.52006 | 2026-09-14 15:46:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 97249cd8-ad94-327e-beb5-4bca7d226a45 | -12.23164 | -40.70316 | 2026-09-14 15:46:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 542c1eaa-519d-379d-8490-6888eb4bad73 | -14.62856 | -40.7369 | 2026-09-14 15:46:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ee561992-af91-32a7-8f67-5b9db188b290 | -12.47723 | -41.41783 | 2026-09-14 15:46:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 4fd341db-ff45-31ee-8206-15311d586e8e | -10.3089 | -45.32997 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 056c5548-4a25-34d1-b986-aa3549391f4e | -14.30354 | -40.81157 | 2026-09-14 15:46:00 | NOAA-20 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| b1f56136-03a3-36b0-b3dd-edc56469e2cc | -11.10831 | -40.47377 | 2026-09-14 15:46:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 6ae0ae5c-f8df-3282-825d-af2e39e0f1b2 | -10.80011 | -46.24647 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 1862efd1-f1e3-33dc-9d78-0828972ddfc7 | -13.57378 | -40.6378 | 2026-09-14 15:46:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 28fe8476-9888-3dcf-b81d-2113352868b3 | -14.35339 | -41.42661 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e662c76d-17db-36d3-a827-e0dc7f359dfa | -14.96056 | -39.06787 | 2026-09-14 15:46:00 | NOAA-20 | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 563f585d-df48-3308-b076-22541b2bc71f | -10.77659 | -46.29539 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 2dc08d15-4db8-3152-9984-e8c00179e021 | -16.48374 | -43.42578 | 2026-09-14 15:46:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| af59291e-17a1-3ea3-a193-5169ae48f8e7 | -14.97029 | -41.49791 | 2026-09-14 15:46:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 45cf71a1-552b-3acc-a7f5-77d2181e9593 | -14.37934 | -45.24826 | 2026-09-14 15:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 247801ad-ce0b-3777-950f-523ba5770b2c | -10.53003 | -46.31416 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b4b4710f-6724-3d33-8c88-1441fe0cf555 | -13.10079 | -42.38195 | 2026-09-14 15:46:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f77dfef3-2394-34ea-814f-a5b123d524f0 | -14.46752 | -41.34927 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a082bdd7-1a39-3392-a6cb-6c37c86b9cbb | -10.64896 | -46.09351 | 2026-09-14 15:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 07d27b84-1dc6-3cbf-b9a3-294db8a4b42d | -13.57235 | -40.62553 | 2026-09-14 15:46:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 98.5 |
| a9ba2124-e46a-3787-baa6-7cb1d8f920b1 | -10.6286 | -43.60579 | 2026-09-14 15:46:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 252c813d-5896-3850-95ac-b078f3e07653 | -10.32422 | -45.28487 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 6b21492c-978b-33d6-b743-14125fd612ec | -14.16463 | -42.20609 | 2026-09-14 15:46:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ab7820fe-577e-3be1-8852-067cfae3bed2 | -11.51216 | -45.75908 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 3d2026dd-9961-3f23-ab28-cecb72615688 | -10.52918 | -46.30696 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 654343de-418f-3e41-9fae-3260616ecec1 | -12.48344 | -41.42372 | 2026-09-14 15:46:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| daf207f9-0ab0-3cb6-9cac-7670f5993cce | -10.65304 | -41.47685 | 2026-09-14 15:46:00 | NOAA-20 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 2415b8ce-610b-329f-91d0-ff6042f9c565 | -14.48131 | -41.37803 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 3a8a4f67-c934-35f8-a00d-2e391b70e6b2 | -10.6517 | -41.47709 | 2026-09-14 15:46:00 | NOAA-20 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 6ba548af-a213-3736-a190-9d0d3097f39c | -16.10662 | -41.76873 | 2026-09-14 15:46:00 | NOAA-20 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 5d32dcd9-974d-3e61-a657-9b2fcfd72113 | -17.26169 | -41.51365 | 2026-09-14 15:46:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 61e33a52-8296-32f7-837f-a075becbc40b | -11.18275 | -42.81387 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| f22cab48-5316-38d3-8f35-9d86a60eb9bb | -14.84683 | -40.88561 | 2026-09-14 15:46:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8ba2ed4e-f083-3a7b-b92b-7c11212b4da3 | -15.19979 | -40.99776 | 2026-09-14 15:46:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| aadc35eb-f017-3a3c-b5e9-cdb7d7b6d98a | -10.77788 | -46.24273 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 3a2ab455-f8a6-3c12-98e0-29dd16e80387 | -11.19446 | -42.81237 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 6bc0686f-75c1-39b0-872b-155664d590c0 | -10.79481 | -46.26363 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 330edd44-5c0f-375b-89a7-636e5cf5912c | -11.18108 | -40.52609 | 2026-09-14 15:46:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 38.4 |
| c103d58e-8f78-3d24-b3fd-6f68b0368803 | -8.57954 | -44.48819 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 36112131-414a-3532-b331-47efa7af56ca | -6.76497 | -42.75139 | 2026-09-14 15:48:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2471ceea-abc8-37c4-bc5d-5a86bbe6478d | -8.17806 | -43.11321 | 2026-09-14 15:48:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 6d9434d5-3285-3d46-814c-15056f95f71c | -6.53241 | -44.08821 | 2026-09-14 15:48:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3a8cfa5a-2aee-3e71-8e8a-d378d196001e | -6.60055 | -42.23659 | 2026-09-14 15:48:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d54fa548-3d96-38c4-8349-f190981a4f6f | -6.12321 | -43.51248 | 2026-09-14 15:48:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 43d82550-0c94-3be2-8a99-4ee3e2434946 | -3.90644 | -44.48113 | 2026-09-14 15:48:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0da28b2a-00a8-34c4-b23a-3bacda1e6e2e | -5.41103 | -42.22247 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0d2fa86e-de61-382d-a848-76493e86656d | -6.04432 | -46.05054 | 2026-09-14 15:48:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| f113ddc4-ac8a-360e-94f9-2a5c38c47673 | -7.61565 | -45.19577 | 2026-09-14 15:48:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c3adda83-ed01-352a-9a53-45b888dba14b | -3.59328 | -41.36348 | 2026-09-14 15:48:00 | NOAA-20 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |


[Clique aqui para ver as próximas entradas](README86.md)
