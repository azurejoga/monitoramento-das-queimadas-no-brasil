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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76682937-696f-3ac5-9144-402f231bb180 | -1.08754 | -53.37854 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a30fff3b-2575-31f4-b487-0ea47c41f222 | -2.30849 | -47.86353 | 2024-11-28 04:23:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 263b8869-9d2f-389e-87d5-e3b95d5fc011 | -1.16266 | -53.681 | 2024-11-28 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2eea1e7d-b106-3cfe-9602-377456b1a1d9 | -1.68732 | -52.47618 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b209813-1069-3ebe-9be8-b033e86a99a9 | -1.68346 | -52.43959 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af022ef3-4c7c-326c-856d-ea5d4a5ebcae | 0.98878 | -50.26656 | 2024-11-28 04:23:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d97d98c9-79da-3f00-87ce-e125f175326c | -1.35042 | -54.63335 | 2024-11-28 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 227234fd-4fac-34df-aa48-9fda578d918e | -2.45852 | -47.60185 | 2024-11-28 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f5490ad-8cb0-326e-b9fe-6250eb8be141 | 2.08797 | -50.62742 | 2024-11-28 04:23:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 636f5cd3-e699-3225-b7b6-7c9c53cfbc1f | -1.73287 | -52.04082 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08dde8f3-61d2-3592-8b51-d66e23aab78c | -1.27569 | -52.16851 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bc85421-0091-3d61-8cc6-538ee06181db | -1.15905 | -53.57113 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08dda62c-8758-30cd-9d0c-80c67253163e | -2.53595 | -47.33169 | 2024-11-28 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1004fd76-01f2-3475-9a1b-d2ad183f7037 | -2.54528 | -46.38393 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ca212a5-b802-3ce1-a915-f9f1c3796928 | -7.75872 | -46.21824 | 2024-11-28 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82f67cad-6f08-34dd-bad8-e8e864ea0863 | -6.10596 | -43.96676 | 2024-11-28 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f04731b3-d605-3802-9b72-f82ef07242c4 | -5.98333 | -45.36683 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0c295de0-a449-357a-bced-e91f5ba1ec38 | -2.74051 | -46.09289 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4e6c046-0e6b-397d-829d-9b908cf43ebc | -2.13833 | -46.48345 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 094da938-97ad-3d0b-bcff-2239a0c5dd08 | -2.68237 | -46.26929 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57dd288a-4f9d-3cb3-aefc-bf5cd6a33736 | -1.40363 | -46.62169 | 2024-11-28 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a19c4222-10c3-370a-afbd-9f29bc2db2a8 | 0.98001 | -50.1251 | 2024-11-28 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4e6d1ee5-f9ce-33d4-b557-77118503e815 | -4.97773 | -49.63403 | 2024-11-28 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a4cb1ee-04cf-3da4-83fe-a4154f335072 | -2.5328 | -47.33173 | 2024-11-28 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdd3cace-660a-3402-92c7-de0107b855c1 | -1.20133 | -51.75338 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5f3b687-49d4-3a70-9d70-b199a2634c10 | -1.66505 | -52.74103 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| aa9e9a82-891a-3e18-a732-a0ce98986b5f | -1.32354 | -51.9275 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 979e5207-11b5-3b3d-9707-5ea08d315322 | 0.98479 | -50.12831 | 2024-11-28 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3055e62d-4c24-3479-8553-6c69ab786c05 | -2.5918 | -46.26191 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a6566c20-b5c1-3179-ba45-2b636f0122ff | -6.83206 | -44.39617 | 2024-11-28 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a553d39-ab28-3270-98d0-d00f2a382bef | -1.4485 | -47.11629 | 2024-11-28 04:23:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddc27679-eab3-3ef2-990b-4cc474773633 | -5.42293 | -47.91931 | 2024-11-28 04:23:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2526a69-b08a-3365-9deb-6b72e2ea7217 | -2.45884 | -46.54027 | 2024-11-28 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d739c05-5bed-3eb8-8f39-bcdda35e3499 | -6.23956 | -47.04154 | 2024-11-28 04:23:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa6f898b-f5e2-33ee-a523-a056f07ce12a | -1.28586 | -51.72822 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4c9a72f-7bd6-30d8-bd0e-8977320b88a6 | -5.82554 | -44.10931 | 2024-11-28 04:23:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5a1a653b-a84e-3b03-b38d-a2585caf89b4 | -6.16101 | -42.62421 | 2024-11-28 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 56d5ca7f-7e49-3048-b818-cbf54d037e3a | -8.36582 | -48.46347 | 2024-11-28 04:23:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce081dfe-71e8-3926-bc3e-a42676ae768b | -1.67548 | -52.48972 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 768e32f5-0073-3d51-bd1e-38a2e7ad6451 | -2.01329 | -46.39856 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40801997-7a3f-365f-a82a-f82cc218e6ae | -1.88908 | -45.46043 | 2024-11-28 04:23:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55745168-d4f9-3d0b-a78b-0e64498ed732 | -2.58726 | -46.20395 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f393ac6-b8cf-3e9e-b34a-d0ba75f15c1d | -2.69652 | -46.11444 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72aa4aa8-b713-3346-9f3e-7b365bd5785c | -2.56369 | -46.41922 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fbf52c8-b97a-3f25-bbdb-cd9b50ad4d91 | -5.43344 | -48.14005 | 2024-11-28 04:23:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46876d06-e2d8-3f24-a74a-50cea4214794 | -5.75805 | -47.9067 | 2024-11-28 04:23:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dea4c6c6-7255-370a-8a2f-527e33d7266e | -5.61683 | -51.28137 | 2024-11-28 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6ee3348-0032-3594-bb99-0765e920ca77 | -1.71662 | -52.48277 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| eb8d1b8f-3a06-395e-8b11-2359210d772a | -1.54861 | -46.04549 | 2024-11-28 04:23:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2802900a-f9e4-34f4-9ddc-92fe5741914e | -0.88208 | -51.7227 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30f9c945-2661-3fed-90d8-fe089d1aa141 | -1.23623 | -51.79652 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5983690-3ee5-3d36-b043-0f051839c7c0 | -2.51991 | -47.40951 | 2024-11-28 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0678fe6b-023f-376a-b929-55544eea70ba | -2.62241 | -46.19552 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7c8d12e-2e87-33d8-98c1-13f40a9022da | -6.47959 | -47.49625 | 2024-11-28 04:23:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15b59b72-eca5-3909-ab0b-970b37652e11 | -6.16535 | -42.62043 | 2024-11-28 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2688dba7-0bc8-35cb-80c1-450e7a1db890 | -2.68182 | -46.27278 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 221ed578-1776-3e3c-8739-380463bb885c | -1.69652 | -52.63424 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6683c192-7541-3152-813a-1d5f49174081 | -5.96781 | -45.35723 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d6ceaa9b-7d7f-32b8-8a60-6cb4a00a9ec2 | -4.0853 | -54.76344 | 2024-11-28 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 570de321-5374-3cbc-81ed-5445fc63cc67 | -6.53572 | -44.65628 | 2024-11-28 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d87de8bb-2e52-33e6-a3eb-d60dd283b784 | -6.16167 | -42.61986 | 2024-11-28 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 96b3e7a9-ea13-3413-8cf5-e3bc6438df4c | -2.05753 | -47.12212 | 2024-11-28 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9aac905e-05a8-384d-b888-922db7bf2d49 | -5.82497 | -44.11304 | 2024-11-28 04:23:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0fefe806-7128-38c7-8413-bc1ebe10a747 | -1.08707 | -53.38147 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8afcc7d0-8ab7-3c1e-a959-62daed2f9df0 | -1.0583 | -52.42632 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7eb9831-dc4f-3c3f-ac8f-228dce22dcef | -2.4801 | -45.87092 | 2024-11-28 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df9a2416-8d02-3b4d-9b7f-5f0ab8fca40f | -6.4801 | -42.81301 | 2024-11-28 04:23:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 397ee3bc-f063-325a-8e50-fc153e645c4a | -1.64611 | -45.23234 | 2024-11-28 04:23:00 | NOAA-20 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6f2792d-0026-3e7b-9600-8befd316e358 | -1.69336 | -52.62316 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| beccf5fc-ce62-3874-a8b9-7a8366b078cb | -5.33971 | -45.66063 | 2024-11-28 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 787dc536-94ba-394f-825a-4790c8674250 | -1.08661 | -53.38434 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dbb9598-95db-3296-b1e1-7124791994d2 | -1.35498 | -51.96619 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d85b49ab-c5f1-301b-b4e4-fc2d72b86491 | -2.28593 | -47.119 | 2024-11-28 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fe1d4f1-df4f-36d8-9934-09057e36cd60 | -1.54475 | -46.15611 | 2024-11-28 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3a329a1-5267-306a-9a9f-04601e321a3f | -7.6879 | -42.97869 | 2024-11-28 04:23:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 98844fcf-7875-357d-a827-d6e83e377afd | -6.09328 | -41.94139 | 2024-11-28 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3e291a9a-a2b3-37cf-9218-0874d653a032 | -1.67955 | -52.43383 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b909bef3-8a10-3ed8-96ed-ad755691b456 | -1.67636 | -52.4538 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 992880c4-1789-3139-b46b-35e2f80250e9 | -1.44791 | -47.12002 | 2024-11-28 04:23:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f9e6698-2a0d-3214-96d0-bf9c1ed94e7f | -6.12014 | -46.59361 | 2024-11-28 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2071dd8e-f912-315c-b7b1-9cb68fb549e2 | -6.70955 | -47.26748 | 2024-11-28 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58125477-f013-35a1-8474-004253263799 | -8.60031 | -47.91934 | 2024-11-28 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8658fce7-34ca-3932-946f-940dc39cd4ee | -6.48659 | -47.89333 | 2024-11-28 04:23:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3890c92-1e76-3ba1-a3f7-abafd9a94745 | -1.15759 | -53.58024 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 638ecf5e-9ad4-3497-867c-68ed0f14ac2f | -7.94685 | -49.75772 | 2024-11-28 04:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0659a271-2dc5-3fd9-8aa7-b71ad23f5ef5 | -2.72689 | -45.4269 | 2024-11-28 04:23:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdd63b60-29a5-31ea-86a3-511848e87ce7 | -6.3773 | -45.69205 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7cb506d-2986-3501-9a6e-90c6d43def59 | -6.48999 | -47.89388 | 2024-11-28 04:23:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0aa9c7b0-df31-35f1-a4ea-0d68fa8713b3 | -2.7179 | -46.23549 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36613499-f727-345f-8cf5-8e14edef7ff0 | -6.86673 | -44.76537 | 2024-11-28 04:23:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47fee8a0-2906-3e85-beeb-217db67d0814 | -2.71458 | -46.29937 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65ed8ef8-3246-3f6a-bf45-9d1c3626d2e5 | -1.58898 | -52.08733 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6c82cf7-d6dd-39f1-9adf-249254ef396f | -1.66986 | -52.74181 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e24dcef0-a7c2-3627-924a-54d24b525c77 | -1.31441 | -51.926 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c2ccf01f-2411-3be3-ba42-4aeef4356c5c | -1.30767 | -51.73633 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27d48683-b92e-3a0b-a624-a46734ea3aeb | -6.36218 | -47.06091 | 2024-11-28 04:23:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 91748a8b-4c61-3038-9896-2f9018a81bf3 | -1.89239 | -45.46095 | 2024-11-28 04:23:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69fba06d-f8e6-32d4-8541-6c7e8c070be2 | -2.31017 | -48.42417 | 2024-11-28 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bd66631-be30-3dc5-b63a-02885674a15a | -2.717 | -46.11408 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e732e53-45a7-309a-822a-0a5fdc90121f | -6.65692 | -47.53192 | 2024-11-28 04:23:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README49.md)
