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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f853002b-58dc-37cc-91bf-ec2275cc406b | -9.64063 | -47.86161 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f172138-1188-3016-a446-76421fac8812 | -14.40436 | -51.70427 | 2025-09-03 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c540c202-697e-3b18-af97-55304a3a958d | -15.5958 | -52.68871 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 929ab5a9-cc6b-3941-8fb7-f6277ecc14af | -11.00892 | -46.82426 | 2025-09-03 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50a71bf3-2986-3278-8421-98b8a6abbb69 | -13.50078 | -46.92296 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fad2ed02-0e0e-34aa-8a24-a9bf00c9c37c | -12.84774 | -48.02697 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 826e1f95-1959-3240-97f4-dbead25838e1 | -11.11778 | -44.65097 | 2025-09-03 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 922b223e-740f-37ab-9240-3bf4e91e5a7c | -15.00576 | -50.06285 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b963283e-f547-3166-b174-90a46d20a1e4 | -10.48153 | -50.35436 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 022388d8-bd55-3f8f-8dd9-e00c34d8ed27 | -15.55355 | -48.40567 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cd21038a-97d7-3fe0-8f33-4aa4e5ca2684 | -13.26595 | -46.89174 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b0426dce-ab33-31dc-b86b-74687f19e05c | -13.73449 | -46.93435 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e5d21fd-7ba1-38e5-ac61-1272cfae810f | -11.37866 | -43.60799 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e03fe879-809c-3ec9-9e87-1c04b1194a81 | -15.12442 | -48.17245 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19e04b93-e1be-3b57-972a-90f77c3bf6fd | -11.5883 | -52.13747 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| b93b5b8e-92d2-3476-8c18-499f27a865b3 | -13.51907 | -51.8035 | 2025-09-03 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e50c67a9-9514-336b-8fa0-c1783992390f | -12.51414 | -49.571 | 2025-09-03 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88498323-1b0b-398c-a7e5-d125b15ea641 | -10.98727 | -46.83693 | 2025-09-03 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c1257b6-1cd3-301b-9775-bd1b1fd1fe0a | -10.73571 | -44.80735 | 2025-09-03 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d689ebcd-e101-3138-ad3e-9a94c1ff51ef | -13.50198 | -46.815 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdea8345-f462-3653-b412-63ff31ce9f37 | -14.40458 | -51.70886 | 2025-09-03 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cf95d28-6769-3606-9332-936e9df6b4a6 | -10.53472 | -50.42987 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d20f71ae-c432-36f4-9ce6-c9d51b8368ea | -13.49139 | -46.82216 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e3f575e-860c-380f-9570-0cd9eb29d78a | -12.2911 | -50.00662 | 2025-09-03 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fdbb334-83fa-34f3-8e57-702c42b54cd1 | -12.67666 | -44.74899 | 2025-09-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e6be87c-50b0-37a7-9940-0db07fa838f7 | -15.1485 | -52.36493 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cfab1f6-c082-3165-9420-ca50a26a3683 | -10.91913 | -50.86353 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5be20970-5deb-34a0-b6b6-08b766271da3 | -9.64632 | -47.85951 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bf916f8-bbc3-3640-bec9-49fc9e0519e1 | -15.00727 | -50.05543 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0fcabc2-4048-3c90-9b4b-bfc4e646f549 | -11.60485 | -52.08925 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a800d07-a8a0-3ed4-82c8-534ba42f2b72 | -10.91933 | -50.8617 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d7920a1d-9d49-3eac-8a3a-8d5d6458c950 | -14.80395 | -48.22285 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e5402d3-8f7c-305a-839a-e424c176d378 | -15.55302 | -48.38298 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 41cb5ca6-b5cc-3781-85f0-4788d8c43c9c | -10.54577 | -50.4368 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9e40e56f-a4f0-3499-8e3e-5b24be069241 | -14.29975 | -53.10338 | 2025-09-03 03:55:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09c6659f-966e-3cc5-8e75-6f96cd0a915a | -15.57093 | -48.31664 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1a2b202b-729a-325a-b082-bd7b192f4321 | -13.47844 | -42.47806 | 2025-09-03 03:55:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b3d154b3-ad4f-307f-b8b3-aad65a85d153 | -13.49239 | -47.02026 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6b38039f-8cea-3fa7-9051-fd8df1773497 | -12.84898 | -48.02033 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 574c2ed3-1a08-3893-bc90-ca298b7d15e0 | -11.6298 | -52.06562 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f16a2670-c458-3a02-a597-b4324ed57534 | -11.58181 | -52.13622 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| a3aaf202-71b8-31e2-8a80-c2ef8ee227c6 | -15.55135 | -48.31572 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f88377b-4344-3bfc-b472-b2e903bd30f2 | -10.9883 | -46.83125 | 2025-09-03 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9d684ccd-6dfa-3f2b-8ed1-53965173e780 | -13.49344 | -47.01854 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 564f6bf3-ce7f-391e-9689-f0563eb523d8 | -12.95198 | -48.07696 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b30fde14-944d-3ee7-b504-ad7330de2c8c | -13.00093 | -48.09496 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 128a25bd-ba7c-3076-8643-3436ff75ea64 | -11.62171 | -52.13919 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d25b2606-d0a9-3cdf-91b1-51eec2313625 | -13.5014 | -47.02235 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a77ca7d3-78fe-3526-b565-2e531606bda5 | -12.8466 | -48.03304 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50fdb8d5-0d53-3122-b56b-60a4cb4078f0 | -15.02085 | -50.04367 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1908a514-3176-3bb3-965b-da05b7ae168d | -11.62353 | -52.06418 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68a15104-dcb5-3438-a925-540bd20594b1 | -15.54663 | -48.3152 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 976bc261-2324-3900-b53c-2a34808bc7de | -12.88933 | -48.08485 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b843d07-0c3f-3ce5-a5ad-6c8e08164000 | -11.62233 | -52.06992 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e1d7f0c-7ebc-3241-8c10-6b1ecefa7920 | -14.63194 | -48.93784 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f8a5aa1-fa3a-3639-95f0-34723221134e | -15.15722 | -52.36263 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c721708-184b-3ee6-b397-094f130f642b | -12.94713 | -48.07569 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15e79d55-2e34-3765-9d30-675f9346cf56 | -10.00404 | -46.90578 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c645206d-3804-39f6-9286-57ece680ff6d | -12.5645 | -48.27021 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d85b05e8-d885-3d10-8bf7-0d90ed8071cd | -10.95187 | -48.14876 | 2025-09-03 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 537332f1-626c-308c-ac2f-8ae2aaaf0ada | -13.30814 | -46.82393 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af41610e-a821-3926-a076-85cd0e19ed3a | -9.63545 | -47.03704 | 2025-09-03 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fbf7962a-ae0d-3066-99b0-b611e53b06e1 | -11.59511 | -52.10401 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e5f10a7b-bbd0-33bb-af7b-763e7a8f6863 | -12.44268 | -48.71294 | 2025-09-03 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6165a8a7-0798-3b75-98dd-1c8770141acd | -10.14222 | -46.26688 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a05b22cb-cca0-3f74-adfd-2fc560d64922 | -14.40558 | -51.70417 | 2025-09-03 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4431fed9-0998-31d2-9c90-d0b9cdbe226f | -12.86906 | -48.03139 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a675c7a-7a60-3d62-bf83-86ee2e6b980f | -13.4869 | -46.8214 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c92e95eb-a23a-31e2-b6f7-37dfadc738c1 | -13.00947 | -48.10366 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4a34639e-fd96-3356-975a-5b21409df94b | -11.57054 | -49.91145 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f73025e8-dac6-305b-8bf7-f01f5dfa8763 | -10.12432 | -47.4374 | 2025-09-03 03:55:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ee41f9bc-47d3-381c-8941-1460a40de168 | -14.79348 | -48.19929 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35d9f5fc-1530-3fa4-9804-b264148a96a2 | -13.5062 | -46.92684 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aabad83f-9f0a-3b0c-b635-2e874b35cd6a | -14.62753 | -48.93358 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b3b1e99-4741-37cc-a1c4-c2bc3e58f029 | -15.89869 | -48.16051 | 2025-09-03 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f770a3cc-0c45-3dc0-a1de-91ec6d7ae1f7 | -11.38165 | -43.61336 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 198bb0f7-123b-3c82-82c7-a9f5e8c34314 | -11.11567 | -44.63934 | 2025-09-03 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 006bd51c-770c-3544-979d-0841708a5089 | -12.92017 | -48.08361 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 9e81923a-9197-3746-904a-a7c45ed0eb08 | -13.20613 | -51.81208 | 2025-09-03 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac4ee5b3-cdfd-3f30-92bc-f9ff4737c527 | -16.2974 | -45.6886 | 2025-09-03 03:55:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eff87f44-d191-3520-ab60-c6e5e0cbf101 | -9.77104 | -49.98174 | 2025-09-03 03:55:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b28db4cd-14a5-3e37-b7d0-a39b2bebccbe | -12.29032 | -50.01052 | 2025-09-03 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b49a516-0610-329b-8fcd-a4b50fbef211 | -14.39858 | -51.70748 | 2025-09-03 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9cf51a8-9f32-3a8c-817f-1e534f8e9442 | -11.63112 | -52.06 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 595eac23-1b0d-3e6a-b014-b1c1f76d3061 | -14.76035 | -48.13884 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98173ea2-8b6d-3a30-9a08-03ce2cd72896 | -12.85279 | -48.02711 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aed3bfc8-ea32-3913-96f7-63aaf4316ae0 | -12.01781 | -45.57431 | 2025-09-03 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 896e7f78-68c2-3907-a51a-267aa6a635cd | -15.01108 | -50.06426 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf6804ab-df82-3572-b6b7-82da9d839619 | -11.59285 | -52.11513 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 9ebd63d4-1ca0-3715-be99-952d06db86de | -11.11714 | -44.65462 | 2025-09-03 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b695e6ae-39df-36f6-b86b-03ad1cbf07a7 | -11.87732 | -40.95175 | 2025-09-03 03:55:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7981470e-f02a-3248-b43e-f17896edb24f | -15.60084 | -52.68273 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ac7f0af-74b6-38ec-ad36-2461af78161d | -10.54326 | -50.41774 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c28056a0-9166-3479-b8fc-733a4663432c | -10.91176 | -50.83566 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99c18b40-e34c-38b1-adbe-da805959cf06 | -9.63021 | -46.12445 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cb83e7b3-85ef-38df-b9d3-9a35996dfb68 | -11.2722 | -48.95024 | 2025-09-03 03:55:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c28ee12-0358-353f-b8dc-005d3fde35a8 | -13.90787 | -48.10514 | 2025-09-03 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0be7de7-a6d1-3bfe-a37b-9b1b0ed33b58 | -15.5541 | -48.37745 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 58b880cf-9e1e-3569-928c-9b1a223a245c | -9.62521 | -47.85882 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a443244c-0ce3-332a-82ff-6e3fae154f0f | -11.36107 | -43.52837 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README39.md)
