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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c74dfcd-e1b6-3b4e-8ac8-9132f9aaa6b0 | -14.80578 | -48.20974 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7790e74a-6f24-342d-81c2-f167e8741c1b | -11.88652 | -50.62109 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22b09525-d392-310d-abbd-dee65b593bd4 | -13.70463 | -46.94515 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0924b3a3-640d-3589-8a0d-46a0a880a8f9 | -10.27503 | -46.49775 | 2025-09-03 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a989eb0c-b80d-3774-981b-cd7eac315e9f | -12.08701 | -43.33389 | 2025-09-03 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 129f3905-7c2d-346a-8dfe-f82c09cfa80a | -13.30606 | -46.85099 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c82bf998-60f4-3997-8570-4bd6dbaf0912 | -14.5802 | -48.04786 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 44ad5ef8-8f25-36bb-af69-0e7b6a2a085d | -12.84127 | -48.06146 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ca8fa24-3803-36e4-9f72-bbf1b7379a37 | -13.89999 | -48.12016 | 2025-09-03 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ceec210-74c7-3383-a537-ff6572dd5305 | -10.49268 | -50.32913 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03202255-58c1-39c6-869b-780a46b753fb | -10.13703 | -46.29625 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db92f461-fbfc-3ea5-9f90-4691e16fd645 | -10.49695 | -50.32185 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62602a47-63a4-3141-80ff-939c0389b4bd | -12.50938 | -49.5664 | 2025-09-03 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 606b96f7-5dbe-3f0d-8e32-f98f95ec585a | -10.72875 | -44.79852 | 2025-09-03 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db9706b5-d4d6-3911-abf6-48d7f1beae74 | -16.40407 | -48.12354 | 2025-09-03 03:55:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69caf1f7-6745-3ce9-868c-051bcda8c2fd | -13.35811 | -46.33888 | 2025-09-03 03:55:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7242d403-f169-3d86-950f-21d1cff4ce7a | -15.54768 | -48.35959 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 023913d5-2ac7-36ac-8c8f-bc86669f1c07 | -11.61577 | -52.06853 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea055926-ee80-3fe2-b261-3115c0b0964f | -10.1481 | -46.28596 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc5f0e1e-2c10-3b34-b51d-cc5c5d406574 | -11.58526 | -52.11926 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| c8ba6584-11ff-309c-8230-d5eb8d319430 | -9.64689 | -47.85635 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba30e6d2-1fa9-3023-904f-59ffe73795b3 | -10.12328 | -47.44308 | 2025-09-03 03:55:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb159cf5-d531-3fc2-848f-72e2cfb55c69 | -12.86775 | -48.02864 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22d737dd-6daa-3f41-8142-f5699f1a79bb | -13.50453 | -46.92797 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aec4fb28-998a-3b86-a87c-51a7dbf0c8bb | -9.6298 | -47.86274 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd817f8a-c2f6-3a12-92eb-7aace072497b | -14.78708 | -48.15453 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| aa06a089-580c-3d21-a9a8-7672798321a4 | -15.55726 | -48.41211 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e38ff5e-52fb-3930-94eb-f383713e8098 | -11.05427 | -45.39967 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f9393ee-4c44-3947-a1fe-2da07579c0f0 | -13.3304 | -46.82924 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39c820c7-fa96-3610-a8c8-c4509becae31 | -12.8828 | -48.03927 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3cbf885-ccea-3284-9efc-ffbf458c65fa | -13.48754 | -46.91885 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c91db2b1-29fd-3d55-843f-369489bcd359 | -11.38244 | -43.6087 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2fca27a0-0a31-3282-b8c2-0d106a322bc6 | -15.59067 | -52.68219 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e11ef34-2894-3463-850b-642c427829b9 | -13.51061 | -47.02715 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63daf4fc-df12-3b9a-a881-88b5504e42ca | -12.99856 | -48.10736 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 80225861-6cb9-3a3f-9879-f9fd37b100f2 | -14.7775 | -48.15277 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 81025af2-d455-3834-9d35-481c1c28acf9 | -11.92346 | -46.66943 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b650f5d5-a38f-3931-a8eb-9f4e7faee961 | -14.73573 | -46.97364 | 2025-09-03 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b81ea30-94bc-3e7d-a689-940320981874 | -10.91077 | -50.84226 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2dfedb7-b0e3-3ee2-888d-1c26df1e5aa2 | -11.58943 | -52.13191 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 43f58358-c0a6-3f3e-8500-ae68ef2602ac | -14.73229 | -46.74973 | 2025-09-03 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c37025f8-3da9-3323-a6f5-ea3369b915ab | -14.79818 | -48.22313 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa0b5e6c-bcf8-3fb2-a43d-87bffe8a3bfd | -10.916 | -50.84632 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 102ef3ab-a301-385b-a28f-b2654d13d99f | -9.39607 | -48.04869 | 2025-09-03 03:55:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f367c02c-6fd7-36c6-8ec2-2a854fbf4e8c | -13.29726 | -46.82255 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e52afebe-5228-3d8e-ab69-2125be0d1293 | -15.56314 | -48.40746 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1a984191-b4a3-3032-9db3-16bac2b4f5c6 | -9.64128 | -47.03256 | 2025-09-03 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdc5465c-d6fa-362c-9493-2b917ae337db | -15.08886 | -48.12642 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e66be0c-5957-3879-953e-620f30388654 | -14.301 | -53.09752 | 2025-09-03 03:55:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e391c12b-06b1-3373-932b-284560b40053 | -11.60732 | -52.14167 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d5341761-c052-3b07-bc1c-c46483e898b0 | -13.00579 | -48.0962 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b71d9b7a-412e-3df7-a1dd-35e994db0650 | -10.13846 | -46.26142 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5b7993f-19ba-386e-9fe8-f4d26119734d | -11.11972 | -44.64002 | 2025-09-03 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6f498063-cc51-3ceb-9234-bc9d5d7375ef | -9.62862 | -47.04694 | 2025-09-03 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8480a006-ba94-3eeb-9ef4-a1b2c5b6ee13 | -9.6256 | -47.06355 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2557c26-1bc7-3793-8adb-3a29a24a1292 | -10.49612 | -50.32626 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83ddb04c-0565-324f-a116-a4de31e6f71d | -13.48165 | -46.8247 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a100f55a-2e8d-3a77-b99a-f5e8345e143a | -11.82225 | -51.45 | 2025-09-03 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3aaab74-7fdc-3566-b9f9-25f683cd73bd | -13.50971 | -47.03191 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 239afa55-0389-3efa-8c2f-920555a16677 | -13.50678 | -47.0186 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 260f62b7-755e-316a-95f7-2c9ec8366217 | -15.09929 | -48.12336 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 003d2533-c55b-33e9-ba55-9e2eb9f52de4 | -11.84789 | -51.41874 | 2025-09-03 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc061176-17b4-35a6-9939-9f2d8de7a92b | -10.0591 | -48.09193 | 2025-09-03 03:55:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53268891-aa34-3112-8977-8676812812e7 | -11.00361 | -46.93465 | 2025-09-03 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08135c1c-8ef0-3ed0-90b4-c09ac9aee716 | -14.76886 | -48.14614 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59c53f84-3879-3f20-a0a4-7fef1fef1229 | -10.94294 | -50.77621 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2a32888-f017-3034-bc5a-c91cf9bdb6e4 | -11.38165 | -43.61086 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4cdf4e8-5d6c-34ff-be1a-99e10c8b1974 | -14.99504 | -50.06042 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3b26acf-d4d7-3b36-84e5-17f0f4d0fb14 | -11.61415 | -52.14324 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3ecb049d-8ff5-3de0-a3ea-90b05378f82f | -9.75563 | -46.91643 | 2025-09-03 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35720f13-c259-32b0-a7e3-b8d2b639941e | -9.63494 | -47.86368 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87f7bfad-d22a-36a9-be53-886d419aac1e | -11.13817 | -46.3444 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e1e8aa91-758d-3751-bc9e-4306d15ced8b | -10.94678 | -50.78479 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db275d7b-6c8b-3c8f-afd3-95bb66ce07fb | -11.38572 | -43.56618 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65bde631-fdf3-3e5e-a65b-b5f6c3700b91 | -11.98223 | -45.88964 | 2025-09-03 03:55:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f97974a-550d-38a0-89d3-a81d785f13de | -10.9513 | -48.15181 | 2025-09-03 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4142a6b-8a8c-33ba-b52b-371c02e19219 | -11.0317 | -45.06217 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52f9e4ac-7400-3ce8-872d-9bf11fc625de | -14.40339 | -51.70897 | 2025-09-03 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9684e296-0b06-3201-91e2-a967d97936fc | -12.6031 | -48.2028 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 321d4a43-6c9f-3dcc-a99d-39764f0f3560 | -9.71492 | -48.31144 | 2025-09-03 03:55:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11e607e8-e309-3608-92a2-7fd574c955f0 | -10.91568 | -50.88056 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62e0625e-d18a-3047-931f-249e6f468a69 | -9.22669 | -47.12704 | 2025-09-03 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4f0d0d95-11e7-380a-a5b8-3c1458613bf6 | -10.55258 | -50.43357 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5591bf22-867e-3ebb-9ec6-0101ebe79020 | -15.71995 | -47.66893 | 2025-09-03 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 841f7bfa-dfcf-3d92-b9c3-351c67ba9f11 | -11.62285 | -52.13356 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8c2b8522-3fce-382a-abbc-ab188943ce47 | -14.60956 | -48.10212 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80afb3c7-c803-3c98-9f9a-60a0e230dad8 | -13.49196 | -46.92014 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3eb92854-ae59-30c1-a7ff-de8c0a8ef741 | -11.61465 | -52.07405 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98128254-9d39-3d32-8034-607c32003cf8 | -11.86141 | -51.46913 | 2025-09-03 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66c1f923-d7a4-3ae6-b305-396e58b3ee12 | -11.1207 | -45.11779 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7d598028-19c4-3568-9ede-a1a47485b9bd | -14.98086 | -50.21301 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52c24bf2-1fbf-3f01-95d7-ca5012883108 | -12.85308 | -48.19026 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5645b0b4-6fb6-3cef-891d-2277eee8fab8 | -13.72806 | -46.9289 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 830d9b0a-ff3f-3fcb-8d5c-5bd4130a2609 | -13.7026 | -46.88042 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41afd755-f14a-3943-ab8f-6cf56396ac21 | -14.56357 | -48.05743 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41b687f1-1ef8-3ef1-a145-1eece5c46c08 | -13.98962 | -49.55646 | 2025-09-03 03:55:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd07fe17-b05d-30d2-95ab-d154b5190a28 | -13.32158 | -46.82664 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff5d1827-2205-3500-8395-a95cfd9f6191 | -14.96998 | -50.21082 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67ef2856-fd5d-3a74-a47d-ab595b403f3c | -11.63204 | -52.05452 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f2ab5ce-19be-3f82-b897-5bbf6be069a7 | -10.10173 | -46.25559 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README45.md)
