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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82820c3f-9989-3d19-ad50-abd9f37c324a | -13.47548 | -47.45846 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a24b1fc-cff9-3a30-83c0-d9f8999eb38c | -11.11417 | -44.02312 | 2025-10-29 04:46:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 45c8ad42-cd60-34a1-90b2-161800643605 | -10.65081 | -47.76455 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a84110a8-c6b3-370d-95ec-837f0757ea3c | -15.19629 | -47.19839 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 204f662f-3e5c-3dd3-8f30-99438ab9b875 | -12.709 | -46.31441 | 2025-10-29 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a1ab5cf2-69ef-34ea-9dd9-31be8c473ed5 | -12.70143 | -46.30545 | 2025-10-29 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d804af2f-f8a1-3f36-aac6-7f33c4c8b4ac | -13.94281 | -48.47112 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6248cad-22a6-3ede-a3c8-82216b47fd4f | -9.12885 | -50.77322 | 2025-10-29 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| defdd35c-f36a-39e0-8c9b-fb1d94abee70 | -14.62032 | -48.42639 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 154a808a-7a42-39a1-a6dc-9ec103dfc8fa | -12.59205 | -52.85513 | 2025-10-29 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c61d8a0e-865c-325c-a647-21aaa604a297 | -13.03111 | -46.73865 | 2025-10-29 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec8bfc9f-8d0f-305d-8a44-35f4efb6a3b9 | -12.08919 | -47.25261 | 2025-10-29 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 149df18e-3995-34fa-aec7-dc37c34328dd | -9.88875 | -44.88466 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63985636-c2fc-32bf-8d72-42e0c369684c | -12.70092 | -46.30935 | 2025-10-29 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 73877ae9-7307-3cc4-ab0b-7001aad348d2 | -10.85483 | -47.9012 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ecd60f15-886a-30c2-af44-741fa42dc26a | -13.03527 | -46.73948 | 2025-10-29 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea5f83a4-ed66-33ef-87bf-c79e955431c0 | -10.96013 | -49.66563 | 2025-10-29 04:46:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59e7956b-dd94-314c-8504-770956537a78 | -14.26176 | -48.12743 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 01b89482-2632-3511-93db-279c1d4bd577 | -13.89616 | -48.5027 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fbe615f-7cfc-3067-b82b-90745e1f530a | -12.2411 | -47.92932 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed00377b-967e-397a-8107-5e9669dda465 | -11.03285 | -47.8455 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec8a8396-9d0b-39e0-ae6a-dba80601bbe4 | -12.10058 | -47.17113 | 2025-10-29 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f323183a-4840-3d5f-b19e-fa2dab4bfbaa | -13.21751 | -47.07396 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76188cfd-8536-398a-a31a-13d9ff3878b9 | -12.3224 | -46.91624 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d3af7e57-da5c-3a38-8905-e621377d069d | -10.04014 | -48.95351 | 2025-10-29 04:46:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a723699f-a29c-35f3-9ccd-c1123a74cb8a | -10.52693 | -50.00955 | 2025-10-29 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7d09401b-3353-3f5c-b96e-928e3bcc0ced | -12.19302 | -46.71819 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| cdf86399-336b-34c5-a221-e7ee350bbafb | -15.21512 | -47.21748 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e51db786-95c0-35fe-b710-fdee1e505fab | -10.74673 | -44.75946 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96fd4034-eded-34c1-9f7e-38cc3f5fe7b7 | -13.93288 | -48.43053 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc52e3be-adc8-3fbe-b666-99b3f6b2fd60 | -10.51616 | -47.7323 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e8e31fa-aa38-3a1d-9a35-797c253b78c9 | -13.63506 | -46.51295 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 152ad1c6-215e-33ba-bf0e-d73eafba286c | -13.64304 | -48.43559 | 2025-10-29 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3490b8c4-1842-3178-8f50-45f53101bdd0 | -14.7311 | -48.17345 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2555a6be-065a-3538-afc2-0004d30384e3 | -10.85655 | -50.09693 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 13c118a1-57c6-3b85-b2de-effc271d21c0 | -12.85519 | -48.62968 | 2025-10-29 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81aed006-f905-39c8-b89c-ea0db4316872 | -10.50473 | -47.73078 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dbff045d-ba8c-344d-81be-57125faf0d3c | -13.61506 | -47.04198 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f412dfed-f88d-3a8c-b84b-c6cbcbe4daa0 | -14.32143 | -46.51745 | 2025-10-29 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 785708ca-e274-3ba3-8ba3-6c15f776a95d | -13.23942 | -47.05847 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00d6e861-8c0d-31c7-9a4f-dfc6e1f4bc42 | -13.56415 | -47.32634 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b05ea62-7fe1-327f-9cfa-b88e9dab1dae | -9.9269 | -47.66682 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc836ce6-45d2-3e64-b43b-a1a8459f4503 | -10.98691 | -47.7302 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7885332-30c4-3a49-a9c6-7e0c38e9ef41 | -9.89924 | -44.90981 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e183cbf-3057-3edb-b0f2-fab7a019e8f0 | -13.0509 | -48.6672 | 2025-10-29 04:46:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f07a9600-b988-362b-b05e-59917b78a2ba | -10.56904 | -49.84565 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 550b2a72-5489-314e-801a-fa160a568313 | -14.7331 | -48.15869 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a42b7a20-3fb9-3b70-9d77-7b98f65cca22 | -13.30882 | -47.46846 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a53b0c4-5265-3f31-b17b-e35d05bcbbe7 | -14.79039 | -46.17661 | 2025-10-29 04:46:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71026829-cfb1-3c1a-9dd1-78e30e5678c2 | -11.03669 | -47.84579 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 59b26262-cdbc-3d23-b736-68b4ccfd68d8 | -12.28887 | -47.00972 | 2025-10-29 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d39c335-c8d9-32a6-ac24-cdfffa5f653b | -12.36164 | -44.06915 | 2025-10-29 04:46:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bb3fa32-2808-3f82-8049-c097964f0bee | -10.76344 | -44.74129 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6b36868-3287-324e-baf7-c35e0cc3cc07 | -15.64398 | -42.91305 | 2025-10-29 04:46:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5702f7b8-6dea-3506-ac27-b484241d1a48 | -11.14246 | -44.93978 | 2025-10-29 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4430c1b2-724d-3cf8-865c-8630154701b2 | -14.62166 | -48.4167 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0be1fa67-b888-326c-94d3-4136ee64fb9a | -10.85647 | -50.14636 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 977a65f8-e6ae-3849-ad1d-2b3be4812841 | -13.35601 | -47.39296 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb119865-0cb1-3148-b332-e1bdf7ad4077 | -10.21383 | -45.9498 | 2025-10-29 04:46:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d12e465-10d5-380e-827b-44dc7fe69253 | -13.65288 | -46.4625 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f76cacb8-abcf-3aa7-be75-f678464d063a | -9.92622 | -47.67154 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c139bde8-a7ff-3293-8cff-ffd66cddaccb | -13.57223 | -49.61071 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c926aab-f5d2-365e-b3c8-06c803d45e77 | -13.04766 | -48.468 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 527921d7-3f15-34a8-8d65-7628065c1ab7 | -10.63826 | -47.9036 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4aa5369c-6c68-3307-b02a-8d8477b0fadb | -13.9423 | -48.44683 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20fa728c-0570-3228-9c71-11c23d49d419 | -10.65946 | -47.99739 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 36d0ba87-4b78-32d5-bff7-176fc0318520 | -13.04383 | -43.82687 | 2025-10-29 04:46:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df5f0afd-35f2-3eed-9531-5f80e8d59b07 | -13.62196 | -47.60574 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b19766c3-f545-36eb-8bc1-a057abb9e773 | -9.93668 | -47.86581 | 2025-10-29 04:46:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64fccf65-2253-34c1-8b11-beb02ad170c8 | -13.9415 | -48.48061 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92046278-e46b-3b0f-8eba-9c5660475061 | -12.05279 | -47.8307 | 2025-10-29 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f8b8cf94-fd46-3e04-aa5f-ce1e5d23b261 | -13.91621 | -48.47115 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05d2eb42-be3e-3e33-ad75-9225679627f0 | -11.99664 | -46.78101 | 2025-10-29 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5be5d886-fad4-3ee6-8829-c46892e8eac6 | -13.63766 | -46.52586 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4b432210-6174-328a-ab82-eb52604a705b | -12.61509 | -48.4405 | 2025-10-29 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 484ad36b-4881-32c2-bde1-78428bf9f3f1 | -15.48754 | -48.4275 | 2025-10-29 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 202eed67-3c3d-34b9-87df-a58687747c95 | -12.14194 | -45.21666 | 2025-10-29 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f3be2b7-8776-318a-937a-2a38e30be18a | -15.11252 | -43.26284 | 2025-10-29 04:46:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e938cfcf-78bf-3f17-97a6-d4e91eef4283 | -10.92436 | -47.60125 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9a33642-4bdb-33b5-a1d1-2abd8f7821e1 | -11.18433 | -45.2181 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a356538b-3cef-3abd-a7ad-ebdb69e1316c | -9.09012 | -47.81234 | 2025-10-29 04:46:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95715466-ccbf-39b3-8f4e-17c9721386fd | -13.56617 | -47.34204 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0f7f87c-a73e-3bf6-945f-46617313f03e | -12.69897 | -46.30344 | 2025-10-29 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3ff2f8a8-ca3d-3515-981f-a3b2fc258e2d | -10.60377 | -49.62197 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac93d595-d027-3058-8e06-1370cb30aa00 | -12.91543 | -45.04612 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73a052f2-b2c0-3ee7-90d8-6870be35279a | -12.19248 | -46.72202 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5b99f5d6-0348-317b-b954-6a8f9b38c844 | -13.32439 | -47.44414 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10c3a5c7-16bf-30f4-a543-f4c29841ea23 | -15.15602 | -47.23579 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a870e33d-05be-3d50-8f51-80829cbecf5b | -13.55212 | -47.32335 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4c3e889-5048-33d9-b9b6-cee62939bd42 | -13.12659 | -47.75343 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4cec324-79b1-38ac-bed1-61f5244bb243 | -10.35567 | -47.56364 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8d87867-24d6-383d-8327-24e2edf29cd6 | -9.90705 | -44.92042 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa3e8b6c-81cd-39c9-8398-006b1ca04779 | -11.78573 | -44.16233 | 2025-10-29 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28d90fca-575e-36e2-9fbc-26cc4c548950 | -15.15754 | -47.23448 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3959ec4e-8a57-3c02-a953-18da14ccdfe7 | -9.76702 | -47.85949 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8a46049-36b9-3f7f-8047-8316d4bed11e | -13.34934 | -47.67623 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83478fce-41bc-3f2f-9366-025d878b558d | -10.65881 | -48.0019 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e1bcedc6-2453-3fe5-a53b-a0625271d6c2 | -8.05605 | -54.92721 | 2025-10-29 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b8a6aec-0dd0-395f-a870-f3e122ec77b3 | -13.01708 | -48.77246 | 2025-10-29 04:46:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e7ac181a-a22b-3d9a-879a-574eb395d105 | -12.4708 | -51.0211 | 2025-10-29 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README71.md)
