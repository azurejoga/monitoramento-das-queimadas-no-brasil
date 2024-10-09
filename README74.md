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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc0fe1f8-b29b-3b5e-9825-e856e22097e0 | -5.87727 | -44.63317 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbcc1bf2-1b9e-31af-9946-9c9dff810d0b | -5.84001 | -44.75828 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e527e3f-373f-3fad-99ed-e7d9b03098d8 | -5.83183 | -44.4627 | 2024-10-09 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 764d7f37-32fd-35f9-99ad-c5423a5b1c36 | -5.81478 | -44.12338 | 2024-10-09 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 08b05938-44db-3995-a82b-6d9bbe8fec84 | -5.81422 | -44.1269 | 2024-10-09 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 83cc6afe-bafa-30b8-ba79-96b30ec9e464 | -5.81144 | -44.12286 | 2024-10-09 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 993d1ef4-5042-3ede-9b1c-9bd399afc92e | -5.81088 | -44.12639 | 2024-10-09 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dd287359-6fc3-343b-9c61-4433f3c3b565 | -5.73648 | -44.017 | 2024-10-09 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8bcdfa9-e03d-310f-89df-7c8569e3995c | -5.72979 | -44.03761 | 2024-10-09 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 133b40ca-d1d6-3aef-9ff6-0c17444a5430 | -5.58573 | -44.87703 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cfd5a4fd-5c08-38a3-810b-36608c39608f | -5.58291 | -44.87276 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a34a7ef-41fc-304c-86d6-3b6b1ce0f769 | -5.58172 | -44.8802 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c95cd9da-d3a1-3533-b860-33ffbdfdff94 | -6.33514 | -45.06726 | 2024-10-09 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e227ed4-d436-358b-aa2e-1370c65c5b58 | -6.25253 | -44.81583 | 2024-10-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 974f8818-3902-3b20-bf0d-b894aad28327 | -6.02825 | -44.87801 | 2024-10-09 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 093656d9-93ff-3f5c-9c1f-8f97c0e1f136 | -5.78838 | -44.92826 | 2024-10-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a199b39-adb0-3e10-8d6c-5e34517cb232 | -5.56615 | -43.69522 | 2024-10-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 231df7bb-ee0e-3e03-b267-7449fd67125d | -5.38393 | -43.64165 | 2024-10-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eeb16188-7012-36e0-8db4-974d3859ee47 | -5.33244 | -43.49477 | 2024-10-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af40ea7c-f984-3b29-bd2a-11ae8b690ec1 | -5.31982 | -43.72448 | 2024-10-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f198e8c-3222-3a9f-8244-959ddebea7ec | -5.31927 | -43.72797 | 2024-10-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a16d03bf-dd52-384d-9dcb-ad748a22c851 | -5.29281 | -43.39916 | 2024-10-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cce046d-30b5-3fd3-9d31-44d1ea880a56 | -5.28951 | -43.39865 | 2024-10-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd661ccd-376e-38d9-abec-21bc2db9fd9b | -5.28896 | -43.40211 | 2024-10-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1201558-ec19-36ec-93d5-259c9172386f | -5.23408 | -43.81445 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d015334c-35af-3b55-bb76-e43b443a10c5 | -5.23353 | -43.81796 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2e4deea-b0e0-3271-9612-1fdfd08ded67 | -5.23075 | -43.81393 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a8b7304-facf-3697-b8a1-bb7387ffbfc6 | -5.2302 | -43.81744 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f707116-5b64-3b63-a56b-93e7613febb8 | -5.22687 | -43.81693 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7e566f5-3a63-372b-bce6-b26ff985bf80 | -5.22409 | -43.8129 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9731346a-8e4c-3c0a-94fe-8735c9605da3 | -5.22077 | -43.81239 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb1e8889-2390-3a7f-bc59-43ccd97cbf89 | -5.62564 | -44.07187 | 2024-10-09 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cb5387f-a45d-328d-a263-afb318e23f90 | -5.62344 | -44.38169 | 2024-10-09 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8381f32-097a-310c-8862-53a5c76c4e81 | -5.62287 | -44.0678 | 2024-10-09 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5eb4657e-3075-3deb-abb6-3eca363627c7 | -5.58974 | -44.87388 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| c361e54a-7aae-3078-a161-64fc53d4f52b | -5.58915 | -44.87759 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c981587f-3051-33ce-ab34-24c491873fff | -5.58692 | -44.86961 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 90d7acd4-396f-30d2-a3d7-64c2a1ace906 | -5.58633 | -44.87332 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 9b1d61f9-6f1e-3434-a9bc-8628eadea63b | -5.55087 | -44.32632 | 2024-10-09 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16a4ef7e-8adb-343f-b2fb-f9600f180caa | -5.53342 | -44.11836 | 2024-10-09 04:14:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55fe7062-c2c9-3bf4-b349-7d7ac588eb39 | -5.53064 | -44.1143 | 2024-10-09 04:14:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3047a3f2-e41a-35af-abd8-92ba834bde98 | -5.53008 | -44.11784 | 2024-10-09 04:14:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 906e7bb8-2384-3a20-8492-cd98bb0a07b2 | -5.45622 | -44.21559 | 2024-10-09 04:14:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 564dc2d1-ae8c-3ca0-b75b-970e01b8b1d1 | -5.38148 | -44.50985 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 190288da-ff6e-3d47-aec9-6cb992db1fd7 | -5.34265 | -44.5264 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1171578e-e35d-399d-9593-c6352373a748 | -5.20412 | -44.53836 | 2024-10-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64b4b4e7-c01d-3422-bb16-8b023736161a | -7.63739 | -44.81714 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8704f432-7db6-3e94-a215-17e6ab4546f4 | -7.63681 | -44.82074 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 085d0e34-8de9-3d83-86b0-63b0299bf1dc | -7.63346 | -44.82017 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46cddc28-68e7-3fbd-8de6-fbc7e9907da3 | -7.6301 | -44.8196 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fb4b4a6-4a3e-376e-ada2-cb41f670d79c | -7.49435 | -44.43583 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d2c20306-d27d-35d1-9513-ffd2aa3ae5d1 | -7.47454 | -43.98256 | 2024-10-09 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 820d4ba8-10db-358d-9a43-8deae58f11d3 | -7.47123 | -43.98204 | 2024-10-09 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e2de2c1-b687-3740-8179-7c24e8fc7182 | -7.155 | -44.21521 | 2024-10-09 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3dd8452b-222b-3bd0-b1d5-6b1463e84e5f | -6.90018 | -43.82692 | 2024-10-09 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdabf799-01bf-3a16-9e78-38b4c0c26080 | -6.89963 | -43.83039 | 2024-10-09 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6cd92262-2030-302f-a76f-12d47db10282 | -6.78359 | -43.8114 | 2024-10-09 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21aafb03-8839-3ea7-ada9-d2a6db8034c8 | -6.78304 | -43.81488 | 2024-10-09 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b49a343f-09b1-3f15-9ceb-2af2ebee2c57 | -6.67827 | -43.95904 | 2024-10-09 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7480c916-b837-3252-9e7d-278ee18c2544 | -6.67772 | -43.96254 | 2024-10-09 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b9f1c72-22be-3986-8c88-7464501ca25e | -6.6478 | -43.87182 | 2024-10-09 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bf61348-9aee-3446-8207-dc89733ceae5 | -6.61133 | -43.78048 | 2024-10-09 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0975ab4e-752c-3a50-92c3-ef510bcd5912 | -6.61078 | -43.78396 | 2024-10-09 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f148741-76f6-32e7-8034-77dc4de61f2d | -6.60802 | -43.77996 | 2024-10-09 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 080a47ab-8b5b-30ac-b691-6dee28b9fed5 | -6.60471 | -43.77943 | 2024-10-09 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7217e05d-2aec-3b68-9ce2-d947d47fc318 | -7.13843 | -44.83386 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c87c3364-9b2b-3db9-a7cb-7e00cb3ce2bf | -7.13786 | -44.83748 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f952d4c-8844-3bd0-9bc2-9c774a4315aa | -7.0994 | -44.4592 | 2024-10-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f2e2466-7720-3037-8c05-a789d448d466 | -7.09884 | -44.46276 | 2024-10-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eedb72ed-00ca-35af-a931-d74f1374af7c | -6.94471 | -44.61761 | 2024-10-09 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ebaac70b-454f-3669-b8dc-ba92ab13811c | -6.94078 | -44.62065 | 2024-10-09 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b25c6cf-3094-3bd4-b13e-a9c06feb2618 | -6.93145 | -44.57132 | 2024-10-09 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f4c6bcf-de9a-3838-8f45-6b0aca16746f | -6.93088 | -44.57489 | 2024-10-09 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7af36ac-4d0f-3d15-bc0a-95681f2049bd | -6.9281 | -44.57082 | 2024-10-09 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| deb98866-6d23-3d1b-8d2a-c3f9bf087a26 | -8.30708 | -44.09893 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34111d85-2829-3f77-83ac-f87074909dd8 | -6.92753 | -44.57438 | 2024-10-09 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96964f0f-8a7e-36e7-872d-d057c6c95570 | -6.73095 | -44.29105 | 2024-10-09 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94a8cf13-0631-39f1-bb62-0b6e2e505d79 | -6.73038 | -44.29457 | 2024-10-09 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d275bdf-33a8-3c56-bcc8-9fd3126888bb | -6.67955 | -44.58999 | 2024-10-09 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 418a3c7d-bfec-3e2c-a666-54834f6bc34a | -6.59857 | -44.16166 | 2024-10-09 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84a472fa-ec22-3427-8235-0afc90d8dae6 | -7.14123 | -44.83801 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adf72be8-7cbe-356e-b5bb-b36235a5c9f3 | -7.1244 | -45.05264 | 2024-10-09 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1731127-2aa6-331f-be3e-ee1f3a661190 | -6.99517 | -45.22543 | 2024-10-09 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c963e56d-568a-3364-b3fb-84ab3db91d3a | -7.63403 | -44.81659 | 2024-10-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac9ef3ef-c7c8-3b75-b7fb-74e90232c166 | -7.30927 | -44.97622 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 682f8f4d-0df1-3c66-9429-996256df459a | -7.30868 | -44.97985 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a075cda6-6413-34cf-8ac0-17dea7e0a7b2 | -7.3081 | -44.9835 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 310776cf-5544-3dd1-aba1-643c1875f253 | -7.3053 | -44.97929 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 947f84d9-5765-3632-a77f-b03512fc511c | -7.30472 | -44.98294 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7921f707-36c2-3e68-9ad8-39884430b554 | -7.29795 | -44.98187 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2fbbed15-3307-32b7-90f2-068dfb628873 | -7.29456 | -44.98133 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e67c5e7-3410-331d-87b1-de2bfdc3a71c | -8.76111 | -44.15421 | 2024-10-09 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03135727-0323-3248-a5ab-41ac6b1098c0 | -8.75725 | -44.15717 | 2024-10-09 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08352c99-fdcd-384b-8e46-9c10e1940c1e | -8.56735 | -44.02348 | 2024-10-09 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b25a0483-7db6-3c34-8cf5-8eba690b7cba | -8.5668 | -44.02695 | 2024-10-09 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa09a677-2358-340f-b2ae-dfa63ccc18cc | -8.56626 | -44.03042 | 2024-10-09 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a62a353-ae6c-35a1-87e7-536d108bf486 | -8.42318 | -44.69469 | 2024-10-09 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b571de1-3fca-384f-b524-dca1c110c8a1 | -8.33576 | -44.11055 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09c79b4a-4f1f-3958-a54f-5e6e38e310a8 | -8.333 | -44.10654 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4deaf65e-d93e-37c4-b748-66d6984d84f7 | -8.32693 | -44.10203 | 2024-10-09 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README75.md)
