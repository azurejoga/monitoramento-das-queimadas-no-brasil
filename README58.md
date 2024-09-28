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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4101d45-ae2f-369f-9fc9-e149f849967b | -16.71565 | -55.9114 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 856ebbaa-6c18-3cde-abd8-eba409dbfcd5 | -16.49095 | -57.37455 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a42b5d0c-0e8f-3aa9-bebf-a3f02f70b624 | -16.48539 | -57.3733 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 439471a6-d707-332d-af4c-826a8b3e845e | -16.48458 | -57.3772 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| eed9cfe3-7150-3425-a6ad-26f792b74b40 | -16.48377 | -57.38109 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7726df16-89e0-3940-b8e6-55a8c56b6c6e | -16.47902 | -57.37596 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7537d93d-4fe8-328c-b03c-d40485883b4d | -16.47345 | -57.37472 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e7df9384-fcc5-33c9-ae58-63656c5b3eff | -15.95832 | -57.20955 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c49cd2e0-02cb-3100-b003-8e0f387e5b92 | -15.95284 | -57.20793 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 842bb8f7-8954-3281-bd0a-0e26170b0694 | -15.94738 | -57.20621 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c14caaaf-8f2e-38a9-ab6c-7e08690ed8e8 | -15.94186 | -57.20479 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a52265e-86f5-34e7-9bee-67a2c2788aa7 | -15.93234 | -57.19471 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc600812-3074-3612-8af8-ca7dce218882 | -15.93163 | -57.19809 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72029f24-d4a7-33ba-a02a-8ba8889848f1 | -15.92692 | -57.19282 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2dc9525d-3ac8-3a90-8e3f-8ad2075a9601 | -15.92157 | -57.19062 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 596bc7a5-7cf6-3bab-b46f-83a77d0e9275 | -15.92089 | -57.19388 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3d75c89-19fe-32a2-9b2f-03fdb4498910 | -15.91778 | -57.18998 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85655c18-464e-3790-86b5-fe95cf791e33 | -15.91077 | -57.1959 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ebea176-70dd-3017-8841-153d8747ce14 | -15.90984 | -57.20045 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ade4facb-ee3b-3c62-a6c6-51e26f3472da | -15.90901 | -57.19501 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e8d1220-59b4-3be3-9da9-ff0388de4404 | -15.90808 | -57.19942 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2dc4db26-0f76-3275-a1d3-fc4a21e1686a | -15.84834 | -57.39805 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1d46d07-889b-35f2-bf46-5b9432edd50f | -15.84756 | -57.40173 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4358b818-9098-3504-bfff-cc9bddf82393 | -15.84588 | -57.39846 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eccf5983-ce9b-3972-ba5f-5b5dc31e0076 | -15.84511 | -57.40221 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5680e7e4-c9e2-314f-a71c-b776eefe56c8 | -15.84027 | -57.3971 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7468f17-f383-30bb-a1bc-274fa0cf7769 | -15.8394 | -57.40129 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab26baeb-9c90-34ab-b540-e84f56477366 | -15.83866 | -57.37635 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45fe08a0-b67e-3838-b7bd-a9f44fba725b | -15.83382 | -57.3713 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e9594c4-1090-3833-85dc-a36905754917 | -15.83318 | -57.37437 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f324644-ec42-3f5e-af57-64a76b7d7b77 | -15.82902 | -57.36604 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e76b36be-fc3e-3a2c-b484-49a52651285d | -15.82837 | -57.36919 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1edabe3-9c3c-3748-9ece-225c048e10de | -15.82772 | -57.37232 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c570b63d-5058-37a9-ada0-b7d0616df2aa | -15.63226 | -57.47467 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad749809-6571-320f-ac62-fb0f44414eab | -15.62483 | -57.48162 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9122bda9-cc3f-348b-8b8f-a55a5a5344d7 | -15.62396 | -57.48573 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0a1be6d-c725-359d-894d-97a7f50179f2 | -15.62292 | -57.4841 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 736b87a5-01a1-3c6e-8cf3-5dd7e2be54c2 | -15.61915 | -57.48035 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd01f262-e811-30ec-a6ff-cadc20b451c4 | -15.61826 | -57.48449 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 423e9aa3-4d2e-36b8-b7fe-9c023147ac97 | -15.61723 | -57.48282 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6b9ead5-aacc-3403-8ab0-a6272e002250 | -15.61346 | -57.4791 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76b3e5e4-0aad-3613-8198-300f8a0e0fba | -15.61239 | -57.47742 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ff41cd6-717b-3e6c-a296-2ea9ea37f620 | -15.60759 | -56.97024 | 2024-09-28 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8da1c103-18d1-3f2d-9ae1-1d731752f12e | -15.60299 | -56.96453 | 2024-09-28 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb55a67a-bdca-394b-9c62-2795d5633265 | -15.60219 | -56.96849 | 2024-09-28 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7479975a-eea2-379b-ba50-c740a086ffde | -15.60168 | -57.50047 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72e7caff-7d50-3ca8-9e85-2950db30c8a7 | -15.59681 | -57.49523 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 27567e79-5ca2-30f0-8bb0-eed769d8362d | -15.59599 | -57.49917 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae22ae55-00e6-36c9-9417-d04818bbb7b3 | -15.59111 | -57.49396 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f9d3fa7-9619-3f38-8c6d-5c7b4fed8a50 | -15.5903 | -57.49789 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dc96e7cd-2481-3761-a880-add25585dfe7 | -15.58622 | -57.4888 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 51a926fb-1171-357b-a073-2b9ae37a5880 | -15.58542 | -57.49267 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5ba0af61-de17-34b5-ac3e-5a0a2516ca25 | -15.56551 | -56.92287 | 2024-09-28 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0d1b91d-3829-3103-8ef2-fc3ca106f398 | -16.93444 | -57.99736 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 84411ff8-8128-3cdf-9751-cfbb2965208c | -16.93434 | -57.99441 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bd6ddab2-c03b-39a6-ad6c-d9aa2b530da8 | -16.93346 | -57.99861 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3a05d9ae-ede9-3cf4-b355-e9a48b1daa0c | -16.92898 | -58.0225 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f0b121e4-7962-3ed5-88e1-6be0900e1403 | -16.92871 | -57.99607 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 844c3c22-22e9-3089-92f4-b0168db18e98 | -16.92817 | -58.02382 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5ac4fa4f-6948-3c6d-8283-89d944a1ed1b | -16.92773 | -57.9973 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a75e2370-96be-358f-91bd-a6d6e0d5d5e0 | -16.92298 | -57.99477 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 54da802f-8148-35f8-b3b6-716c5f75416a | -16.92289 | -57.99179 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b8d7fb10-32f3-3d5c-af3d-a677ae6c92d1 | -16.922 | -57.99599 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b9ea3009-db02-3f1d-8122-93e85ae6ed50 | -16.91725 | -57.99348 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 11d5fc0e-93cd-3a72-a03d-e3bc59e19aca | -16.91628 | -57.99467 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| af4339ca-2646-367e-a394-2b87e6b0816d | -16.91055 | -57.99335 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f7511da2-a674-369f-890e-f48a1e4a327e | -16.90966 | -57.99755 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c1cf2959-6dac-39ac-96a4-15849d64ad79 | -16.90531 | -57.96144 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c1312c65-21cc-30fa-81d8-9719079cf72d | -16.90482 | -57.99205 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cb93e25a-38ca-373f-a21e-dc9cd9ee1594 | -16.90442 | -57.96561 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| dbaddbf4-4b55-38c4-950b-ae2531d56087 | -16.90393 | -57.99625 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 463c9b03-5c44-369d-a1f0-bbbb912fee3d | -16.90353 | -57.9698 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f2b523b4-cceb-37c1-852d-0ea1ca9462d8 | -16.90265 | -57.97398 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5f181cef-001f-3a76-bc6f-a52674e1f84e | -16.90176 | -57.97818 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| d50e0534-c5eb-305e-8bc9-3c7f257492e9 | -16.90047 | -57.95596 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| bf102706-b81f-3821-8038-0298583fcfe9 | -16.89959 | -57.96014 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 998f05b3-e13f-3547-88ee-61cb3bad511b | -16.87887 | -57.72321 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 740aa2d0-b315-3d70-a899-eef37d074c52 | -16.87235 | -57.726 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 71e19a87-ac1f-398c-99b1-d738b1aeaaff | -16.83714 | -57.74209 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2ebd4a1d-20ca-3b8d-a604-60ba1c7051ee | -16.83149 | -57.74081 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 02943c1b-c1b0-34a5-95e1-ff156c04c9e8 | -16.66893 | -57.45192 | 2024-09-28 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2839b2e5-c195-3bd5-aa1d-0da78215799c | -14.89806 | -57.97826 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9f7c40b8-0e6d-3204-815e-97d63a383997 | -14.89718 | -57.98246 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e8fea390-8da1-3334-affb-a42ff601a3a1 | -14.89211 | -57.97699 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e39c4e43-f397-31d3-8ea7-7b43a4b07a24 | -14.89119 | -57.98135 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a0d65529-3f09-3698-98a6-a37e2ffc0baa | -14.88966 | -57.97599 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 183059ef-2a22-3eda-a44b-dba73adb80c5 | -14.88875 | -57.98041 | 2024-09-28 04:23:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4c35ea5a-7362-30d4-821e-a207e72c2fa9 | -19.39182 | -40.1706 | 2024-09-28 04:23:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 38ca267c-62cc-3049-9f07-df1d5d0c8055 | -18.31586 | -39.92563 | 2024-09-28 04:23:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 616e8088-e8c9-34e6-830d-364c25300473 | -17.93662 | -41.20278 | 2024-09-28 04:23:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e54a6be5-4c18-3a0c-b266-428945a98dc8 | -17.93611 | -41.20699 | 2024-09-28 04:23:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0f3918f1-9105-39c6-a329-00df8ccbfed5 | -17.77707 | -40.45489 | 2024-09-28 04:23:00 | NOAA-21 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c1edb820-98c5-330a-a961-ad8489a7a669 | -17.77649 | -40.45957 | 2024-09-28 04:23:00 | NOAA-21 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bdcf2109-5654-38f3-8717-6ce5163e062b | -17.58695 | -41.35332 | 2024-09-28 04:23:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 689a9fda-a11c-37ec-9196-1d23065262c3 | -19.0073 | -40.43539 | 2024-09-28 04:23:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 21197a89-39cd-307d-8654-4030c07cfd81 | -18.79354 | -41.61489 | 2024-09-28 04:23:00 | NOAA-21 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 2e2ea0ac-3491-3e12-a5ce-eb0b26a24036 | -18.79305 | -41.61886 | 2024-09-28 04:23:00 | NOAA-21 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 609f96ac-46ee-32a8-946a-d3c97a49a613 | -18.76432 | -41.19631 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOÃO DO MANTENINHA | MINAS GERAIS | Brasil | 3162575 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 2db89aba-899a-3951-8542-f787cbbb71ee | -20.2654 | -41.30125 | 2024-09-28 04:23:00 | NOAA-21 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5e5ca0db-784b-3409-97f6-4993c711ff1b | -20.26467 | -41.30275 | 2024-09-28 04:23:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |


[Clique aqui para ver as próximas entradas](README59.md)
