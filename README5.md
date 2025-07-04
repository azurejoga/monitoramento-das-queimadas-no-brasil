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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64c4023c-c0e8-3517-9d71-21b29a77570b | -13.40239 | -47.83942 | 2025-07-04 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c7ff13e-8653-30b2-a353-b12e42994264 | -13.69181 | -47.74832 | 2025-07-04 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b7807b5-c02d-31f7-8478-d17881ed41a4 | -6.85061 | -43.30479 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 288bf99f-c937-385c-b4cd-1a515fb81aa9 | -7.30462 | -45.36636 | 2025-07-04 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efaecfce-f667-398e-a92a-5bb850f88976 | -11.24495 | -44.89051 | 2025-07-04 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3b35802-7d7a-36b3-93c9-1f13766d0b6a | -8.24086 | -43.74708 | 2025-07-04 03:49:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 07fe4892-a681-3d71-acba-50f492018f0e | -13.25938 | -46.89449 | 2025-07-04 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be2428ac-0d28-3e96-97ba-a8f1d75e4845 | -8.44622 | -49.6355 | 2025-07-04 03:49:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| abbec1e3-fdb2-336e-b102-864114eb0f4c | -9.79381 | -47.74743 | 2025-07-04 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5124f427-1c93-3eae-9560-75ad7192605d | -10.85718 | -42.46985 | 2025-07-04 03:49:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2007d05-5cad-3058-b0a5-b71e6c601f6e | -11.92957 | -45.39066 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 867fa33e-955a-3796-b6f3-c83051475e52 | -13.39799 | -47.83393 | 2025-07-04 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1200970f-3435-3717-adea-44090b863957 | -11.91477 | -45.39343 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93d7e1d4-afcb-3627-8ce7-0975fee93a7f | -12.10988 | -43.65633 | 2025-07-04 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38b6b786-b71c-322b-a936-24e461398d9b | -6.89248 | -43.21608 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c0ab217a-d11e-36f9-b839-bfd37ca5e000 | -12.26919 | -43.65837 | 2025-07-04 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b3f9904-fdad-3193-937e-7a9bb1e89d3e | -13.69175 | -47.74749 | 2025-07-04 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1112793f-76c5-3abb-97d9-b35553905138 | -8.48461 | -49.85757 | 2025-07-04 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29b1a797-a541-302e-8ded-f0e6eec365cc | -9.59019 | -46.75949 | 2025-07-04 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2a417a8-39a9-355f-bdfd-63720ac8c14c | -6.72225 | -44.33721 | 2025-07-04 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7c8ca81-3dea-3a9d-bf96-7d632a553acc | -11.19999 | -48.99851 | 2025-07-04 03:49:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3164efd-8707-38aa-a55c-a02f99db8f3b | -7.07917 | -43.21167 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a3a82204-503e-3d74-9aff-f8a7ea75503b | -7.19621 | -43.58443 | 2025-07-04 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63bb37c1-2895-37b1-be6e-25c793398853 | -9.79869 | -47.75235 | 2025-07-04 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16842462-1b79-3891-aa36-d4a0f5ca0675 | -6.88744 | -43.21951 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| bace9c68-2366-31fb-9932-151a689753ce | -9.79453 | -47.74352 | 2025-07-04 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c38ae20-f026-3f94-9db3-a7c82faffa6d | -12.20073 | -50.94307 | 2025-07-04 03:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1cc4361c-b05a-3371-b0d5-5e14076783e8 | -9.80196 | -48.25254 | 2025-07-04 03:49:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ee02e19e-2f55-35e8-9ef3-9615a747c824 | -12.16791 | -45.53025 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50fe5d61-a272-3ff5-bff8-d287f2dc95ca | -12.93288 | -47.14567 | 2025-07-04 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86b22082-8c22-3fc2-8ddf-b872af107ec3 | -10.58713 | -49.46055 | 2025-07-04 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 67146c09-c587-3292-b94f-246c172c277b | -7.2222 | -43.08706 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4d064771-6db2-3e66-ac31-9c8d4e680386 | -11.92123 | -45.38416 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1013ef80-1e62-33f8-91cf-43af9917243d | -9.74094 | -48.35345 | 2025-07-04 03:49:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 973aec80-105d-3591-ae12-d5eadefc49d1 | -13.39351 | -47.82886 | 2025-07-04 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3ffbee8-7ba5-3a76-9e3f-07d621da9201 | -6.72682 | -44.37737 | 2025-07-04 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21a7d977-9799-3a2f-a322-873998188a58 | -7.29964 | -45.36542 | 2025-07-04 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78ac202a-19b9-31ca-8ebd-c77e66b46d87 | -9.08722 | -48.32125 | 2025-07-04 03:49:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f6033cc-4fbb-3a9b-bf4d-c44fae584a48 | -8.8675 | -47.27821 | 2025-07-04 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55021405-585c-3de0-a74d-47c7e20adbe5 | -7.23434 | -43.0933 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c87595b6-c8ad-3604-aa8b-cc6fab825e6a | -7.22579 | -43.09182 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| ec32d247-1666-3608-95b2-22e3e3ea56de | -9.08642 | -48.32549 | 2025-07-04 03:49:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 42b70e68-76f1-3c28-a87f-700167f97833 | -10.65119 | -44.48672 | 2025-07-04 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3bf903cb-6a54-33e9-9ee2-114137bb3eb5 | -10.25867 | -48.15122 | 2025-07-04 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08a2e7ec-5742-3418-8ce3-5a8c9702222c | -12.16452 | -45.53105 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27a78702-d1bf-3eae-bba4-0981be93bf20 | -9.61329 | -49.02172 | 2025-07-04 03:49:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b92c2483-be8e-380c-9738-4df655bbce4c | -8.44849 | -49.62921 | 2025-07-04 03:49:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1665c8c6-11ce-3060-866f-00a5e72aeeb8 | -6.89318 | -43.21189 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a57d984d-e7e5-39f8-ad68-8d33e8e451e6 | -9.78312 | -48.57087 | 2025-07-04 03:49:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c21a7a7d-5209-3e57-ad8a-834347663026 | -12.42467 | -43.7246 | 2025-07-04 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a333ec32-7fc5-3dcb-b5ef-731d19f8a3e6 | -10.64596 | -44.49035 | 2025-07-04 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 77a648b9-b56b-301d-b8c5-8ab297b52cc0 | -11.92319 | -45.39954 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 613088ac-a324-356d-81ed-379ee315c29f | -9.6142 | -49.01699 | 2025-07-04 03:49:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1141be3-f76a-3577-b854-71229bb18dfe | -7.35029 | -44.84054 | 2025-07-04 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| feaf224d-7e0a-316b-893d-4e9031fc342c | -7.22511 | -43.09586 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8b8c3038-7921-36a4-b3df-52c5c823e346 | -11.92497 | -45.3898 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 24b115fc-ae02-315d-8bb5-5ec0aa9896c9 | -10.98368 | -45.10676 | 2025-07-04 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04657bd1-6fa4-3287-8a47-2c5fef31befa | -10.55614 | -49.13369 | 2025-07-04 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f766d0f2-9da6-38fc-94de-f8ccacf5a520 | -10.98279 | -45.11168 | 2025-07-04 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 939e5465-4560-31c7-af59-301d2e6f875e | -13.39867 | -47.83048 | 2025-07-04 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0252c26-eeec-32c6-badc-dd1128b05542 | -11.91855 | -45.39884 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ef9e7b18-6eaa-3ece-bf5c-3df5515ae736 | -11.92869 | -45.39552 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4514347a-094e-33e6-94f4-29f2bd73627d | -7.09415 | -44.38717 | 2025-07-04 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae39726a-b05d-3c2f-bf5a-5ef8886537d9 | -11.92211 | -45.37937 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9bd7242c-924c-35ca-907c-1d41accb81b3 | -13.697 | -47.74944 | 2025-07-04 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbbb579b-eb6e-3e80-9f74-4fe243e1d1d5 | -11.92294 | -45.37482 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 248d2181-9a7f-3f2a-a102-46fc67031a80 | -9.80189 | -48.25515 | 2025-07-04 03:49:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62f771f1-da20-3833-bbee-d916230c360b | -10.36955 | -47.55973 | 2025-07-04 03:49:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 123ec2f0-fc8c-32c9-b662-5976e1d9f22f | -10.24852 | -48.15342 | 2025-07-04 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6a26ea0-00cb-3f46-8202-9d85cc6a3f25 | -10.59327 | -49.46174 | 2025-07-04 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8e091c08-8d1c-38d8-8909-5a82c530968f | -10.24427 | -47.67972 | 2025-07-04 03:49:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c193d0c9-f91b-329d-a86c-bb5c0b0939c7 | -11.2059 | -48.99958 | 2025-07-04 03:49:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 027ea943-8d04-3eba-baa3-cd73c969aa76 | -13.40157 | -47.84359 | 2025-07-04 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 297f232e-6881-322d-85db-257e174485f7 | -7.22151 | -43.09109 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4a935fec-3ccb-3930-a00c-2e79300b4e1d | -10.98546 | -45.09694 | 2025-07-04 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b6da892f-481d-3898-b07d-903f14d84086 | -7.90295 | -44.53277 | 2025-07-04 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d9cc71a-365e-3da1-a454-4692cb89d72a | -13.38756 | -47.83128 | 2025-07-04 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a985573e-c435-301b-8eee-1791d26f1cc2 | -9.75577 | -48.27533 | 2025-07-04 03:49:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5630bfec-da46-3edb-a264-8efab01e9095 | -11.84142 | -43.79672 | 2025-07-04 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cdf4580f-8f5e-3db9-a0c6-4fbb9c510fa5 | -11.52644 | -48.95735 | 2025-07-04 03:49:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43a74876-b1af-351e-b573-002c3d01c023 | -11.44511 | -45.11622 | 2025-07-04 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 983578c9-1ef3-3c11-8de4-7e2ed813fd68 | -11.93153 | -45.40611 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f0759d7-1fb2-3eaf-a583-1eef72b3e9ab | -9.78899 | -48.57206 | 2025-07-04 03:49:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3344b173-fc03-3c15-9403-6ab9c2bf293f | -7.84088 | -44.21582 | 2025-07-04 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 767a024a-1551-3fa6-957a-bfe2e9a4eb66 | -9.20408 | -45.33868 | 2025-07-04 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98618a43-02cf-3425-909c-c29d1205a540 | -10.98457 | -45.10184 | 2025-07-04 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e1337e2c-d81b-36d4-bbe5-807379122ff0 | -12.93474 | -47.1358 | 2025-07-04 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bc4c43a-f3f3-36c3-b791-9597a485681f | -7.9509 | -44.84509 | 2025-07-04 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62be8b66-0cdb-3f71-a621-8da6cc2b7fc7 | -12.42533 | -43.72086 | 2025-07-04 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 41165db8-7baf-32bd-bf17-f3dcc6c454c4 | -9.79225 | -47.74528 | 2025-07-04 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0c6ce2ef-2d60-343c-bfed-4aa60f89120c | -11.9223 | -45.40443 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5cdc9049-fe2f-3fec-8560-6d1bc960c933 | -11.54786 | -47.86444 | 2025-07-04 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5377deda-450f-38d2-bdfe-175762fc76f8 | -7.22871 | -43.10061 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 50b6d654-478f-310f-89c6-6a42b59d6d94 | -11.44596 | -45.11146 | 2025-07-04 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 268c4675-76dd-37ac-9268-3fcd5e7fcd74 | -6.9231 | -43.05993 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22fc5bf7-1507-3896-951b-12679854ec00 | -9.2089 | -45.33954 | 2025-07-04 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50115e88-0d2d-3b8f-8376-50959bb9e6fc | -7.21791 | -43.08635 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e43de45e-f3cd-32b4-881b-8271ac0950b2 | -10.34617 | -47.29107 | 2025-07-04 03:49:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9b0b890-8350-372d-bc17-8ceba4847295 | -12.20153 | -50.94434 | 2025-07-04 03:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f72ec91b-c96b-3dc2-8cf8-72682d3b37c4 | -12.93994 | -47.1362 | 2025-07-04 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README6.md)
