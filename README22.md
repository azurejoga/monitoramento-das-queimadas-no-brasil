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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04b92548-5567-3d1d-bff7-f429eeddb935 | -9.9859 | -44.16389 | 2025-10-25 04:00:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53b46866-0980-3ded-a9a7-586641282dec | -9.08612 | -47.81411 | 2025-10-25 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c77a8878-0cfd-345b-9cd0-a652b5f9e4f6 | -9.32829 | -45.18344 | 2025-10-25 04:00:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e4190ad-3af2-3bff-b3a1-17460ef52c74 | -9.71832 | -45.42688 | 2025-10-25 04:00:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e12f1a7a-f7da-3a59-ae09-cd1176e9114d | -12.74263 | -43.46246 | 2025-10-25 04:00:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d22aec2-e74a-3e54-bcdc-23db08e7c70e | -14.20418 | -47.30191 | 2025-10-25 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0a83b7d-1ee0-3ae0-a7e8-fa2f85e9dfb8 | -10.52068 | -44.18052 | 2025-10-25 04:00:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13061191-eac5-3fd2-9207-8c6ab4afcafc | -14.86577 | -48.09397 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 64723db3-7c16-3f0a-b373-e54e4ab0fc8e | -13.35438 | -47.42248 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dffe6a16-78c8-36cb-a2c5-79a9174d1cd9 | -9.08668 | -47.81099 | 2025-10-25 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74fc45d9-50ed-3fb8-aa16-71043ca391c7 | -11.59329 | -45.06807 | 2025-10-25 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6f175e4-5098-329f-b04d-5aed8c5db078 | -13.54009 | -47.56054 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd14aae2-7299-326d-9a4b-7ed1fb9f27a1 | -14.93186 | -48.13221 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3606740e-87c7-3001-aa51-3ca1f0d2414b | -9.69807 | -45.38814 | 2025-10-25 04:00:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05717a79-8652-32fc-b38f-90110cdfd1ea | -15.52993 | -45.70548 | 2025-10-25 04:00:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5cb3615-fbb1-3399-922d-0d34e71d67ad | -14.86893 | -48.0772 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94948b19-9bf3-301c-9390-b7a439da6404 | -10.61792 | -52.1902 | 2025-10-25 04:00:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80bacb8d-45a7-34ac-a061-1876b84b0090 | -10.06325 | -47.08668 | 2025-10-25 04:00:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b29a00d-ad11-350f-bf73-49eb949ed5d8 | -13.28685 | -47.49695 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ca82063-e331-3470-8579-fed82ccf546c | -13.3368 | -47.90968 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11f27e15-4a2b-3608-9d83-6d104f8b33a5 | -12.05377 | -46.40701 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fab612aa-0e16-3e47-bb57-c779a604f892 | -15.30257 | -42.96472 | 2025-10-25 04:00:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 31361813-ce6a-30d3-bc52-2238e5177be8 | -13.65107 | -44.22955 | 2025-10-25 04:00:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00933d6f-133d-34e9-8370-e9e6f382ef24 | -13.79602 | -43.2248 | 2025-10-25 04:00:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 78ed8b17-f1c2-3078-bf34-3035594a223b | -12.25499 | -47.44286 | 2025-10-25 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ccb73399-83b0-373c-b487-01050ee40836 | -12.1927 | -43.57907 | 2025-10-25 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc32c716-e6c8-3015-944e-354d7a096c57 | -9.99734 | -47.59553 | 2025-10-25 04:00:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9bd9f77d-b401-32ff-9455-57dd501dc0ee | -10.39692 | -45.31557 | 2025-10-25 04:00:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cd26735-9a49-3a28-86cf-bc6dca14b2a3 | -14.98577 | -43.54913 | 2025-10-25 04:00:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5380eefe-8488-32aa-9f89-10331c425f55 | -13.40666 | -47.36042 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7498eee0-9934-35de-bb4a-91c545bf3e10 | -10.84567 | -47.91826 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9c7e178-c00b-3229-827a-0c2dd697a256 | -10.97821 | -44.72823 | 2025-10-25 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7d486c2-5b9f-34da-a03a-204667f74b28 | -10.00003 | -47.1026 | 2025-10-25 04:00:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59a49136-7590-3453-8515-ea4c9f9bb56c | -10.94769 | -50.29709 | 2025-10-25 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54e5d364-a107-39e9-98aa-57ea1fa521b5 | -10.63722 | -45.23281 | 2025-10-25 04:00:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09602cbf-255c-3637-a1ff-c696394a4547 | -10.47087 | -50.2086 | 2025-10-25 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed912577-03c0-3997-831c-70070d52eaed | -12.29709 | -47.45634 | 2025-10-25 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed1a6ccd-3916-36dd-b52b-1cd6106b5e19 | -10.6443 | -45.24223 | 2025-10-25 04:00:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e0befc7-1eb0-3a7a-9e28-45ce9627b026 | -10.71406 | -44.74591 | 2025-10-25 04:00:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9520190-7c61-39d6-b12b-4628afd1cf16 | -10.87607 | -48.03837 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18fe80f5-ea7f-3c86-87e5-8de485c29dc9 | -14.39666 | -51.51875 | 2025-10-25 04:00:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d41dfbee-6eaf-3510-aaae-b919e68dd0cd | -10.06419 | -47.08147 | 2025-10-25 04:00:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1df3003e-5268-3a0c-a98d-311ae22ddd17 | -14.87159 | -48.08929 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4d17cae3-e92b-3f73-b0ed-7cd9697b3dd5 | -14.71989 | -46.61973 | 2025-10-25 04:00:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8e713ea-7178-3588-9237-6f85de6ee0bd | -11.42931 | -44.67428 | 2025-10-25 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1710e915-dfe9-3909-9b77-72194e96ccb6 | -14.72839 | -46.60039 | 2025-10-25 04:00:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c931bb13-dc55-381d-9cba-ae91f84c70fd | -11.98679 | -43.31451 | 2025-10-25 04:00:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a305155-a9cf-37fa-a0bf-4198f55a8136 | -10.86797 | -48.05378 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14e48d2c-c28a-3f05-b508-4fbf17c1b1fd | -10.64358 | -45.24621 | 2025-10-25 04:00:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a644103-a416-3553-8eab-62d9b8aa5222 | -13.68383 | -43.48809 | 2025-10-25 04:00:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a39126f1-6a2b-399a-85a8-92d860425761 | -10.56469 | -44.93463 | 2025-10-25 04:00:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 135bade9-2866-334c-a542-0d17e14cd6d9 | -13.06771 | -47.5639 | 2025-10-25 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5f485b8-bf98-33db-b0bb-f248764788f3 | -12.83647 | -48.63589 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5eceea1-8fc0-37ae-af3a-5f3605afa638 | -13.32469 | -43.09804 | 2025-10-25 04:00:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7919cb58-be2c-3d44-9d07-7c02e5d36150 | -13.45209 | -48.60178 | 2025-10-25 04:00:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0039ceb9-30e8-360d-9189-013f8423f4ec | -11.5807 | -49.53645 | 2025-10-25 04:00:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0ced828-aa02-3cda-b48a-99a685e8681c | -12.14569 | -47.0196 | 2025-10-25 04:00:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 343c9da0-e1d3-3cac-8ff2-b103a01330a3 | -12.36473 | -48.12428 | 2025-10-25 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14afda36-8ebe-3e63-b768-982f9356b202 | -12.8296 | -48.67113 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 389c1c91-db17-303d-b37f-96295690d163 | -12.29504 | -47.46371 | 2025-10-25 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f6f52b1-77b5-3fd2-a858-feac950c001d | -10.41863 | -44.50145 | 2025-10-25 04:00:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3443ac3-24ba-347c-9e9b-e1dfa2d38716 | -13.21743 | -47.78353 | 2025-10-25 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 664e29ec-d612-32bc-a5e7-ef1692e36819 | -14.86108 | -48.09259 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7762873d-ecef-3142-9848-91cf25b2dd40 | -14.94938 | -43.36522 | 2025-10-25 04:00:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e85c9bb1-3f51-3052-b651-8430fa2af118 | -10.93071 | -50.41598 | 2025-10-25 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b6b7037-ea91-3b74-9e16-ba0c9f7f7098 | -14.47862 | -47.90444 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29f218bd-959f-398f-b623-4cf8ce887f43 | -12.12149 | -46.70946 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5aeb7466-881b-3b6f-b292-b307ac3c8ad5 | -10.62448 | -47.9191 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c9e7534-12fb-3d30-ae8e-77fa483547b5 | -12.31247 | -43.84839 | 2025-10-25 04:00:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38ceb15f-8998-38b8-b47e-dc56b16311ac | -11.43272 | -44.67861 | 2025-10-25 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ee95ed9-7d2e-35ad-839c-5f48219c2801 | -14.72043 | -46.61878 | 2025-10-25 04:00:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eba61360-35cd-3ffa-a656-2015a95727c0 | -11.50232 | -44.00402 | 2025-10-25 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e18178a6-9b89-3e8f-b42b-818b8a87ff1e | -14.89371 | -47.86816 | 2025-10-25 04:00:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dfb89395-4417-3e66-842a-9488d9081c30 | -15.19957 | -43.78459 | 2025-10-25 04:00:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c0e9fb5-417a-309c-aa6b-5f0081705ea8 | -14.74632 | -46.60048 | 2025-10-25 04:00:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 980ec70e-635a-3f12-a360-13c4b7e7afa7 | -13.32049 | -42.41776 | 2025-10-25 04:00:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bb7c7085-b475-3d90-aeeb-f2795493f30c | -13.00376 | -48.54942 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c48f56c-e471-3842-957c-e88d5c29abbb | -12.19717 | -43.46278 | 2025-10-25 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8be4b29-6817-34d0-aa34-1473713f880b | -12.10779 | -46.70685 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27a778e2-c664-39a5-a723-212105423b6f | -14.86202 | -48.08419 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ac45aaa8-1a53-3697-be1f-5a8479675497 | -12.28921 | -43.78062 | 2025-10-25 04:00:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2897f397-8627-36da-b29b-94ee6d88bbe2 | -12.07107 | -46.39884 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe32b73e-6431-3b3c-9a80-5a322b166864 | -14.86789 | -48.08269 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b0b1240-0d74-3634-9721-53351e373ae1 | -14.76942 | -43.08277 | 2025-10-25 04:00:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 9.6 |
| afe98fab-b190-3362-9983-bffb7a3129d7 | -14.86348 | -48.10189 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| ae497300-5cec-3d5a-b3dd-ee243acbcd6e | -12.05823 | -46.44324 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53052121-56e3-3a31-8e30-c22f5e9ea5ca | -14.49413 | -47.05942 | 2025-10-25 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84658818-a513-3f2b-bcd0-ab9fe49d68b2 | -9.25402 | -45.58596 | 2025-10-25 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a236cdc-17bb-3aef-bb4b-ff8418fd7f5f | -14.9375 | -48.1286 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a5eeb3b-8634-352a-b341-f17ba58c537c | -10.87076 | -48.05113 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa0f2850-98e9-3850-9d1c-83c3c61f9521 | -14.15951 | -44.76038 | 2025-10-25 04:00:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e424e61-4d55-3979-bc5c-a0c59bd76553 | -13.62822 | -47.61684 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84b7687f-1328-3c2f-8b47-bdf09827e8ef | -9.71906 | -45.4226 | 2025-10-25 04:00:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac128e9d-d495-30eb-a58d-844638ada88d | -14.92495 | -48.14242 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 505e694b-3ee2-30f6-bb5d-d8df78305364 | -9.59022 | -46.88238 | 2025-10-25 04:00:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 535ee708-c13a-3bc3-90e8-d29b17b76c43 | -10.6673 | -48.0695 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23d9b73f-0e5d-3807-9b58-54684f976e6b | -10.9823 | -44.72898 | 2025-10-25 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38ef2f6a-ba03-32ef-ae87-0ad86663f0bd | -12.22676 | -43.31177 | 2025-10-25 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa68099b-e224-3cb8-84fa-0e886881db7e | -13.83439 | -48.50975 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aee2ce68-15dd-31ac-9be9-9024db816eae | -14.44235 | -48.07178 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README23.md)
