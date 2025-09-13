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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49d72842-74ab-398c-bfd3-b65c0476bed1 | -8.9176 | -46.1565 | 2025-09-13 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 232.3 |
| 7c79fb99-d6f2-3629-9c69-83d21ab52086 | -14.4394 | -47.3206 | 2025-09-13 14:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 6b100851-5b8e-3620-852d-62845aa7b6d7 | -10.4438 | -50.6272 | 2025-09-13 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| f9d46768-2a66-3563-a12a-c8b544e21963 | -11.0953 | -51.3866 | 2025-09-13 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 8ea92799-6385-3b57-a987-29cffc44f8ce | -10.3888 | -50.5051 | 2025-09-13 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 2b1b6c12-e430-3a78-9bd5-27fa02f476d3 | -16.5679 | -55.1801 | 2025-09-13 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 96.7 |
| 4e3b3b21-d2d7-3852-bf66-0be7f7088711 | -16.0061 | -47.9329 | 2025-09-13 14:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 103.7 |
| cf7dff6f-b6df-39de-b65b-d226428a9431 | -11.8698 | -46.7627 | 2025-09-13 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 49792017-745e-316b-8374-beb1a3147175 | -17.4346 | -49.2258 | 2025-09-13 14:00:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 003d24cc-00d4-3eba-8496-ca2596e18d6a | -12.0657 | -47.6091 | 2025-09-13 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 15918160-1e7d-33e7-95e0-45a83dc1f4ca | -9.6919 | -47.5438 | 2025-09-13 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 5c95fbd1-6f43-3ea8-b1bc-8700efad3e58 | -11.3835 | -47.3206 | 2025-09-13 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 6b44f5db-a846-38ab-bb5b-e7f904ca3f2f | -11.8656 | -50.6005 | 2025-09-13 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| a05e1f16-1a9c-31d3-96fc-43a28cc9c277 | -10.8972 | -45.58 | 2025-09-13 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.0 |
| fbee9eab-96f7-38eb-b3ea-749763ff4e1a | -15.1165 | -52.4918 | 2025-09-13 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| e49d3b0c-abff-3145-8869-32035ed35156 | -14.2905 | -46.0693 | 2025-09-13 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| b06a1aa9-acb3-3266-860d-3db602a22256 | -14.29 | -46.0924 | 2025-09-13 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 186.1 |
| bb276f25-c2f0-3a63-b9ed-9051c768f3e5 | -12.1044 | -47.5816 | 2025-09-13 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 158.4 |
| b8293d04-d9a0-3bb9-a32a-c6619389c0fb | -15.0432 | -50.1556 | 2025-09-13 14:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 961dc134-2a64-3454-855c-0eea9d5dc465 | -11.7391 | -46.5779 | 2025-09-13 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| e4f97785-e7bb-3b82-8fda-b57a9ebb916d | -14.3095 | -46.089 | 2025-09-13 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 151.1 |
| c6212634-ae56-3436-84e5-a5a7b4bb75bd | -10.5484 | -47.2242 | 2025-09-13 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 11de4761-af7b-388a-bc90-8a387f95c700 | -7.3954 | -44.3539 | 2025-09-13 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 77fd9d8f-2c05-3b25-a57f-644a9c6ec716 | -12.8259 | -47.9486 | 2025-09-13 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 993ea852-7b2b-3d12-9c1b-bad7f3bc9048 | -12.9398 | -48.0213 | 2025-09-13 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| b1b25cee-d9b9-374a-b7df-4a015627873b | -14.2088 | -46.2669 | 2025-09-13 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 107.3 |
| a3a68429-32d6-394a-989f-3e39f50366d6 | -11.1234 | -50.7262 | 2025-09-13 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| f280f65e-e061-3619-a24b-f133df078df1 | -12.1236 | -47.579 | 2025-09-13 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 97a868a9-b104-3952-a2df-6ede98dc9b4a | -11.3644 | -47.3231 | 2025-09-13 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 2bdd511e-0314-34da-94bf-5b5464a2feb6 | -14.31 | -46.066 | 2025-09-13 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 65a4908b-f534-32d6-9e97-3bcf256edc42 | -14.1703 | -46.2505 | 2025-09-13 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 119.9 |
| ea91dcfa-44e3-354d-a9f7-677b9489a07e | -13.9168 | -48.2998 | 2025-09-13 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 40.3 |
| a08625da-1d8f-38bf-aadb-c7483c6a0abc | -13.2535 | -43.752 | 2025-09-13 14:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 80ee995f-0d12-32b4-ad6b-4790bdacd171 | -10.8976 | -45.5572 | 2025-09-13 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| e59d2704-dd6a-37db-aa00-0b3a251a5a70 | -13.4708 | -51.7712 | 2025-09-13 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 0b8908a2-aed7-31d9-bb03-048dde920976 | -16.0056 | -47.9555 | 2025-09-13 14:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 73.8 |
| dbbe1641-9058-3fd8-a501-f0a59eadce4f | -10.3701 | -50.4857 | 2025-09-13 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| b520e130-51cc-3eda-a0d4-3a089ac1e1b1 | -14.394 | -52.9245 | 2025-09-13 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| cfed4cef-9048-3562-8e25-357614b3db47 | -10.4249 | -50.6291 | 2025-09-13 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 2a8e8fa3-3128-3b8e-9696-82e7f4308d73 | -8.9368 | -46.132 | 2025-09-13 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| d8a36385-979b-3f45-afd6-098d254a0c50 | -16.4903 | -55.1484 | 2025-09-13 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 103.3 |
| 87656ee1-b076-3626-bd98-4445e54e86e2 | -14.4133 | -52.9221 | 2025-09-13 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 4c81661b-ca8a-3b62-84cf-ea830a27c31d | -17.4142 | -49.2519 | 2025-09-13 14:10:00 | GOES-19 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 8f0b991c-a577-37de-9c37-05846917418d | -7.4513 | -44.3946 | 2025-09-13 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 91593ebb-c4c0-336f-97f9-fa3d7d633c18 | -16.0791 | -50.0151 | 2025-09-13 14:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 6fd8887e-2472-3435-98d4-48861538a35e | -10.8976 | -45.5572 | 2025-09-13 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.4 |
| 2e9d241b-a828-372c-9807-12ba67e192f3 | -11.8853 | -50.5554 | 2025-09-13 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| d244fa36-fd74-3bef-8251-1935f961c421 | -11.2692 | -51.1354 | 2025-09-13 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 86623f7a-ed00-37ca-b5d8-3fc7b1efb809 | -11.8465 | -50.6027 | 2025-09-13 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 1dceb8c9-1ca7-3590-90a0-b5d92498986f | -8.9176 | -46.1565 | 2025-09-13 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 66fbc0dd-9d4e-3c8f-a7ea-7af0a1f9ba3b | -13.8979 | -48.2804 | 2025-09-13 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| b67af602-4a28-3acd-9733-b9f025230bda | -10.8567 | -48.1827 | 2025-09-13 14:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| dcef4369-21ad-3d56-b4df-45bf71b63426 | -13.9185 | -48.2105 | 2025-09-13 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 135.1 |
| eb4cce28-6bd3-3b49-a45e-e64166c7aa08 | -12.8259 | -47.9486 | 2025-09-13 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| cfa9c4c4-29b4-3971-be21-bf4741434337 | -16.5679 | -55.1801 | 2025-09-13 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |
| a0dc7974-2988-336f-9eb6-ce0e2f064180 | -15.1605 | -50.116 | 2025-09-13 14:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 268.4 |
| 5eda7578-95ef-3a88-b871-253336de684b | -8.5159 | -45.1349 | 2025-09-13 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 7c24d871-5876-3924-85fe-22e5bdf5f7a8 | -13.9375 | -48.2299 | 2025-09-13 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 107.4 |
| b6ec82b7-7af4-37ac-85fa-f1170dc908f3 | -13.9181 | -48.2329 | 2025-09-13 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ae2d0063-8b2f-364f-84c4-2c4d28812491 | -9.7108 | -47.5418 | 2025-09-13 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 51d6796a-fb70-3caf-996b-6e6ca414f939 | -11.095 | -51.4077 | 2025-09-13 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| d25fb5dd-e32e-3015-a59a-cef37cbf8d4b | -18.0065 | -46.9499 | 2025-09-13 14:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 2b344bae-35ac-3d20-8019-5545adef6afe | -13.2535 | -43.752 | 2025-09-13 14:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 170.6 |
| a48ef574-87ce-385b-9d31-6c104d085375 | -11.331 | -50.7888 | 2025-09-13 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 7d59339f-80fb-344b-b9d9-d9b6e277c1fa | -15.8845 | -47.2286 | 2025-09-13 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| b3559c22-53ed-31d4-94c0-9e81a3c4814a | -22.1964 | -49.6194 | 2025-09-13 14:10:00 | GOES-19 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.6 |
| 34946dc0-12ab-39a7-a03c-4ba46ff5b84e | -15.1169 | -52.4705 | 2025-09-13 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| e6915126-db8e-3393-ac4d-668fc4429bf0 | -11.8468 | -50.5813 | 2025-09-13 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 256.6 |
| 957a3d0b-9e28-3dd1-b178-15414fab132f | -15.8648 | -47.2322 | 2025-09-13 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 912d57b1-1b5a-3f12-8a71-20276dfa867c | -15.0436 | -50.1337 | 2025-09-13 14:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 10389a63-bbbc-36be-a361-e5ce37215ce0 | -14.31 | -46.066 | 2025-09-13 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 6df1faa3-eedb-3819-86ee-a17bbdf718f0 | -14.4364 | -48.4421 | 2025-09-13 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 1890e199-bf0f-3ee8-89da-8a3b6fb34eba | -11.3838 | -47.2982 | 2025-09-13 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 0144e63d-dc4f-34ee-9426-b44581d0f11c | -15.1363 | -52.4679 | 2025-09-13 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 56978833-ea85-3eca-903c-45c4dd5ff3c2 | -14.3095 | -46.089 | 2025-09-13 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 80bcb224-1ab7-357e-9a17-c9041b8b4c14 | -9.4819 | -55.9601 | 2025-09-13 14:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 656b8a84-6339-3b47-8bc1-ed72c107d2f3 | -10.8781 | -45.5826 | 2025-09-13 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 63eae5ed-c958-318b-ba1e-3bbe563ebbab | -8.9179 | -46.134 | 2025-09-13 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 74ac15ee-03be-3ce5-ad48-689e34cd4bc4 | -15.1165 | -52.4918 | 2025-09-13 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 26a34658-e35b-31cd-8b6d-5fe4712e7198 | -16.5682 | -55.1592 | 2025-09-13 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 136.3 |
| d23b66c8-f813-3cfa-a1c7-fdb14d603cb5 | -14.394 | -52.9245 | 2025-09-13 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 190.7 |
| ecdb69fa-7eba-39ea-aa99-d4739527166f | -13.4708 | -51.7712 | 2025-09-13 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c274417e-281a-386e-90e4-c60fcaf62f44 | -13.9379 | -48.2076 | 2025-09-13 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 6cbf21de-e977-3107-b9e7-64e96b5fc83a | -9.6919 | -47.5438 | 2025-09-13 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 947492ff-d3db-3fa6-bede-d037ec569199 | -8.9365 | -46.1545 | 2025-09-13 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| a842017f-7c1a-3672-aa13-48382ed6de72 | -12.9398 | -48.0213 | 2025-09-13 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 0c70e7be-9309-304a-88de-736dc2115647 | -17.4346 | -49.2258 | 2025-09-13 14:10:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 132.1 |
| f26df649-07d3-3491-90c7-22a84c015122 | -14.4368 | -48.4198 | 2025-09-13 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 5c0bf996-d691-34ad-8291-5bd97f589a6e | -13.9168 | -48.2998 | 2025-09-13 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| bc7064ba-370e-3a86-b67d-ff2e16890d23 | -9.9757 | -50.3548 | 2025-09-13 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 889b0b8e-09a8-3977-85e1-27f80a1fb5fa | -8.956 | -46.1074 | 2025-09-13 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 227.8 |
| 28872a82-9d79-3234-8160-f32e25b0bfea | -12.1236 | -47.579 | 2025-09-13 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 73034078-599b-3c1b-9384-59e120022f3a | -10.3361 | -48.8106 | 2025-09-13 14:10:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| fd139260-0be3-32b8-9de6-1452cdb8fc36 | -12.8452 | -47.9459 | 2025-09-13 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 185.6 |
| 054a58d2-4d9b-337e-969d-ca38e072464d | -18.0466 | -45.418 | 2025-09-13 14:10:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 130.3 |
| ecf31d60-611a-3072-bebc-16361299077f | -10.7133 | -46.3752 | 2025-09-13 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| a499b942-b7fa-3dd9-bf42-6325336d8f11 | -15.4713 | -47.3256 | 2025-09-13 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 7a7fbc49-4948-3a9a-b121-07be93720ebf | -8.9749 | -46.1054 | 2025-09-13 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 203.7 |
| 073e8ea9-8fc6-3a8c-8ebf-03532233a8f4 | -7.3954 | -44.3539 | 2025-09-13 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| f5a2c110-188d-38b3-a290-d3be83e4c23d | -12.9591 | -48.0186 | 2025-09-13 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |


[Clique aqui para ver as próximas entradas](README132.md)
