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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a048233-5499-3503-bf01-135e6f869ff5 | -20.42677 | -45.99507 | 2025-07-08 04:17:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1b42cf5-27cd-3c37-9249-481c007ac433 | -15.26184 | -51.53133 | 2025-07-08 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 703408db-b194-3888-b8b1-49f95c2ed621 | -9.81066 | -48.25544 | 2025-07-08 04:17:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd81a69c-0381-333a-8e82-cf70b4ae7204 | -13.90367 | -42.13457 | 2025-07-08 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9840eba9-047f-31d4-acc8-4d05bbad798a | -23.3386 | -46.77152 | 2025-07-08 04:17:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6afab603-26d5-37c1-adec-b865d051d065 | -11.87806 | -58.71681 | 2025-07-08 04:17:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 494af227-a52e-3a43-b857-af1fbce5207a | -12.02884 | -57.08298 | 2025-07-08 04:17:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a89a6208-668c-37b0-8e19-b7177323b470 | -11.7816 | -45.21503 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2f5b2c9-3b74-370c-a08b-87070693d6b1 | -11.29596 | -45.27322 | 2025-07-08 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2db837ed-1ef6-3297-88b5-66c1e5e70537 | -14.0132 | -46.21827 | 2025-07-08 04:17:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4d456fa7-e400-394f-a9c7-2b2cb57bf032 | -20.7771 | -49.86673 | 2025-07-08 04:17:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1a91e253-ab53-3b75-88cc-6d5b3668daad | -18.04069 | -39.92451 | 2025-07-08 04:17:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3d73b8b0-9524-3e00-9bf8-4dff4565a2aa | -16.05081 | -43.80213 | 2025-07-08 04:17:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b92c267f-6f0b-38fc-a140-f41e31c240df | -13.89364 | -42.12886 | 2025-07-08 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5d2c99be-c06d-38be-89e0-a3c9f743e9e4 | -13.40401 | -47.8902 | 2025-07-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c98f40e9-2ad6-310e-8b07-05912882209e | -21.17996 | -43.97993 | 2025-07-08 04:17:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 093db82f-9a67-35f6-95a4-3e6a0e066ead | -10.64713 | -49.46803 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| caa365a2-a6c7-3893-8ae7-f31ed43ff0a1 | -12.28488 | -50.10927 | 2025-07-08 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eacea9e-e303-3619-9de0-29a50ddd517c | -10.83283 | -54.03128 | 2025-07-08 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 304663c9-c8bf-3cbd-b39a-45e39bf548cf | -10.82808 | -54.02648 | 2025-07-08 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 985e06b4-3e19-39ea-9dc9-44e2cc725ce7 | -17.09198 | -45.62297 | 2025-07-08 04:17:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a73f94f0-9eda-37d4-8d7a-de5a36141911 | -17.09428 | -43.80259 | 2025-07-08 04:17:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d91f65eb-cfb9-3999-8df6-29a5e246d4cf | -10.27917 | -49.55884 | 2025-07-08 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b148e9c-a278-3998-bd23-cbe36fd938ec | -10.58204 | -49.12278 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d42178d1-abef-3840-8d87-fa1d8d720985 | -15.26019 | -51.52977 | 2025-07-08 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48c2e7a6-a047-3c7b-bd34-bdc8c3dbbac2 | -11.42423 | -45.10847 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| c2fb7c3b-2986-36f9-ac35-5465527f9510 | -22.10461 | -43.20108 | 2025-07-08 04:17:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 047b9e7e-0b1f-31ec-a303-3cb2d010a58b | -12.29378 | -50.10698 | 2025-07-08 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d7fb6ae-a3da-3654-b3da-0703da9ce7d1 | -19.2009 | -55.75713 | 2025-07-08 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0c6d6a72-189a-3c48-9c9f-59a77832777e | -10.57868 | -49.11862 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 39313ce1-18a9-3738-a2fc-9b53e7b3b375 | -12.58215 | -56.98464 | 2025-07-08 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| afb5fb50-bcdb-3e48-9a41-d2f800b89e96 | -13.41325 | -47.87905 | 2025-07-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9483350-dfe9-350e-b470-824050aa7fc1 | -10.81805 | -49.49529 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e57d5060-307d-3879-b855-f79cdee77006 | -21.18895 | -48.93908 | 2025-07-08 04:17:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c70da2be-e0a6-371d-93b4-864a16b28df4 | -13.02373 | -46.29331 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca879fde-197f-3edb-844b-a480df962741 | -13.41748 | -47.87572 | 2025-07-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd51090b-f9f9-312b-bb51-5d69fab6cf18 | -13.89954 | -42.13816 | 2025-07-08 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1af8a2bc-e22a-3bab-ba62-76fe23de5e9b | -21.08008 | -45.44212 | 2025-07-08 04:17:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe71d2c9-dcc1-39d9-b62b-878256c874f3 | -10.65246 | -49.46145 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b78fe85f-bcd4-3afa-8824-202b2583c2c7 | -13.64775 | -46.81608 | 2025-07-08 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4b6e880-4178-37f8-addc-999d352ee4cb | -13.10604 | -46.88428 | 2025-07-08 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4ed6812-0fb1-3daf-a19b-73a882dc18a1 | -15.24821 | -51.53306 | 2025-07-08 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38d2a06d-6063-3510-9913-21dfbe975cbf | -23.71406 | -47.4401 | 2025-07-08 04:17:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0fe0a84f-be87-3eaf-9894-0d760a9501d0 | -10.64436 | -49.45998 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65c42da0-0517-38c3-af0c-b77eb771b530 | -14.04708 | -46.24255 | 2025-07-08 04:17:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e315d810-0ac2-3d26-bb7e-aee509c0ddf7 | -10.63838 | -49.47025 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7ef310f4-6747-3873-9e0c-6234a4aab7de | -11.43693 | -45.11417 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 22a6a6a9-a9f6-3318-b271-2a2cc3efdf8a | -10.21404 | -48.4696 | 2025-07-08 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06b7dd27-c4e3-3b2d-bf7c-5cb8395d7409 | -10.82556 | -49.54927 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47a93b73-a8b1-3e25-ad07-a4b3bb1ff791 | -10.365 | -48.72268 | 2025-07-08 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd563638-1085-3f52-bd5f-f5cadac48253 | -10.99914 | -42.78436 | 2025-07-08 04:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cd8a9ff1-6140-3e24-8a24-312b288f394c | -10.57807 | -49.12211 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 3d0f5a56-8d72-3271-b786-c5325202e907 | -10.36331 | -48.73253 | 2025-07-08 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3980189e-4036-3bcb-837c-9f2ca1e4dee6 | -12.06118 | -43.50764 | 2025-07-08 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05d5cc69-8575-3502-82e0-9b67d90df24c | -21.27438 | -46.05105 | 2025-07-08 04:17:00 | NOAA-21 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| baf9b7aa-7fa4-36e9-9ffe-0276a4ae07bb | -11.80776 | -44.27132 | 2025-07-08 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a476f7e8-9333-3223-ba82-322b37d0f51c | -21.30401 | -49.45285 | 2025-07-08 04:17:00 | NOAA-21 | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| af1133d7-a340-3c35-aa28-5cb3873a764d | -10.39358 | -52.17216 | 2025-07-08 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1de87f8-0470-3628-afbb-d876f08e626b | -18.63931 | -55.73125 | 2025-07-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 53343fdd-baef-381a-b993-812c88abb98d | -9.87182 | -48.46797 | 2025-07-08 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bf6c15c-a09d-3d43-b39f-a6ed261eda35 | -11.43254 | -45.09895 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9a97cfd4-c186-3b93-8e69-eae9fd17b8f6 | -13.01538 | -46.77184 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a9436d8-f3b8-3dc3-8041-4adbaf0521f6 | -11.42754 | -45.10901 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| e24c2de1-53d2-35cc-82ac-2183b2015191 | -20.72252 | -56.65396 | 2025-07-08 04:17:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e32c58b-ebeb-34bd-b867-b1af53824c32 | -17.6776 | -42.74211 | 2025-07-08 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94174750-3308-3d45-92e7-43d9144526d0 | -11.90255 | -44.92352 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8d118cc-3b24-3b89-a056-567c1fa1873f | -21.30583 | -49.45874 | 2025-07-08 04:17:00 | NOAA-21 | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 889f0b6a-4229-373c-88f3-af6c85a6842a | -21.17928 | -43.98144 | 2025-07-08 04:17:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1387e2c1-ad3c-347e-b324-507af8f5c610 | -13.90427 | -42.13043 | 2025-07-08 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 25abffa9-dda9-3aed-b577-213f9a56448a | -13.01387 | -46.75955 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d5616b6-1e72-3009-ba88-29446080d66f | -11.89925 | -44.92297 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1567fb8c-fb6d-3dbc-8ba2-cfa0b05d81f2 | -15.2525 | -51.53388 | 2025-07-08 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 341cd73c-e7b7-351c-a8e3-8387b2281346 | -22.1556 | -43.26312 | 2025-07-08 04:17:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 86d8a696-987c-36af-9dec-f091bea20551 | -15.61837 | -46.46066 | 2025-07-08 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9939aa38-21ae-3e88-8092-87d94c2d263b | -18.64075 | -55.72438 | 2025-07-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0f29a27b-f3e3-3a04-a3cd-0a53e2c8e798 | -21.26411 | -45.68878 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4a1f6c61-20b2-3a1e-8010-4e7ed7150697 | -21.49563 | -47.27131 | 2025-07-08 04:17:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd2c5e91-329d-3eaf-9a50-8552fa9ea30b | -19.7524 | -54.00094 | 2025-07-08 04:17:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3180363d-7d51-3f95-866a-7995fef0b50d | -13.03847 | -46.28794 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77ca1366-f5b3-3de0-917c-df69421dd972 | -10.41492 | -49.77005 | 2025-07-08 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86430dba-37e9-33be-b67c-6dc43dc7da2a | -12.96803 | -47.82431 | 2025-07-08 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 679f0778-e356-37f4-82ff-840e5f8cc87b | -11.84355 | -43.79758 | 2025-07-08 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9f18f28-1119-3f9a-951d-ab50ad129848 | -21.51927 | -45.2565 | 2025-07-08 04:17:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c1e56909-2118-3fcf-8154-be1c6a239bed | -19.75341 | -53.99589 | 2025-07-08 04:17:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9510f934-e7a1-37da-bb74-0d092dd8812c | -21.30678 | -49.45771 | 2025-07-08 04:17:00 | NOAA-21 | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4f6f68cf-199c-316e-91cc-77e3fb28aa47 | -10.58143 | -49.12629 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f55e335-6001-38c5-8208-46b8fb3fee50 | -21.58079 | -45.71116 | 2025-07-08 04:17:00 | NOAA-21 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2e2eb408-547f-38a3-840e-45a6a1d3d857 | -11.42866 | -45.10195 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| f222ac95-1876-3283-90cb-6a48cffc80d6 | -11.84077 | -43.79351 | 2025-07-08 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 941f7c9c-fdb9-3563-b25a-54767574e62a | -15.59902 | -46.87687 | 2025-07-08 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f66bb0b-27a8-3134-a1f9-3fc4df442b6a | -14.19181 | -45.50774 | 2025-07-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad317429-a0c5-3dab-802f-5788a5fe0852 | -16.6831 | -43.88448 | 2025-07-08 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 182cee53-8659-36c8-a0b3-2cfd862c28eb | -11.4281 | -45.10548 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 2242c58d-ac41-353e-b7bc-736e3875f7d0 | -12.99094 | -44.88146 | 2025-07-08 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fecd7e8f-e6f0-3074-b2ad-b6f8182eb1b4 | -10.34956 | -49.92233 | 2025-07-08 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e06d1786-d653-3ac7-8274-256f63e0bcb0 | -21.04477 | -55.99939 | 2025-07-08 04:17:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6251d4cc-cf64-34df-8860-5ac30106f70b | -21.5159 | -45.25593 | 2025-07-08 04:17:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ad722716-a973-36d1-83e3-1e42ea8b3255 | -10.97789 | -45.11208 | 2025-07-08 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0871ca36-f773-3632-ab5a-e5d81198a699 | -11.84409 | -43.79404 | 2025-07-08 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a025bd8d-1582-31ff-9c0b-ad7c21f355de | -14.27314 | -53.23265 | 2025-07-08 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
