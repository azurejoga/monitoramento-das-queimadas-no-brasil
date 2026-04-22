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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f961c32e-9e21-3b63-a761-a462a2f686b9 | -11.99945 | -47.76612 | 2026-04-22 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07679131-3917-3000-abd9-8ecd58765a33 | -18.42398 | -49.59455 | 2026-04-22 04:17:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| ad4f8c9b-76e4-3aa6-82aa-adc16c7d9e9e | -20.86178 | -48.63062 | 2026-04-22 04:17:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 19e545c7-3e0b-3a58-8fb6-198bde0428d2 | -11.7768 | -43.66012 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4f96df55-78df-3c0f-b269-25058b4fa74b | -11.76849 | -43.64794 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c65e0998-2bd2-38f6-9495-6ac6d3f8e5c5 | -13.37815 | -45.33525 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8331818d-fcc3-343b-ba53-c506ccb1c8d6 | -12.01359 | -45.23114 | 2026-04-22 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 767d2448-ede6-3c42-a171-f5039ab3450c | -11.78066 | -43.65712 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d1d0707-bfce-328c-b28b-ec6e2cae7c8c | -15.5155 | -40.85266 | 2026-04-22 04:17:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8b892442-c301-3eab-a5fb-58c830d41213 | -12.85627 | -43.77785 | 2026-04-22 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1d8c16b9-f968-3060-b97f-c16a6ebfce4e | -13.39144 | -45.33745 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9dbd21e7-9563-3fc3-a8f2-52ebf9c302f3 | -13.38479 | -45.33635 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04a59046-04b8-381e-9ae6-492934a45a3c | -18.41946 | -49.59853 | 2026-04-22 04:17:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 904da72a-c65c-3353-b2df-1eae2e2e8219 | -18.40319 | -51.43392 | 2026-04-22 04:17:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e08c063-0b52-3ea3-a4a5-f2f9b02e1886 | -13.38147 | -45.3358 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c29ec5e4-6ff3-3a70-b174-fdae9505bf28 | -12.02806 | -45.22618 | 2026-04-22 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0423f44d-4fb2-3c5b-a760-74f6d7e0370b | -13.5299 | -44.03834 | 2026-04-22 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f655a41-f085-3e06-a8a2-3b8bbcd86259 | -18.42315 | -49.59923 | 2026-04-22 04:17:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 402c160c-0a47-3306-98f2-db37f6c6809a | -11.4839 | -41.21181 | 2026-04-22 04:17:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b09fac2e-58b1-3fbf-8620-7d13ad7431df | -13.91128 | -47.38917 | 2026-04-22 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52871819-0152-3d69-98d6-a5a87146dfca | -11.77349 | -43.65959 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bf602764-3087-31e8-8e14-1cbcb76fd9e6 | -18.48866 | -51.67321 | 2026-04-22 04:17:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 990a258e-7a2f-3a79-b14e-71770d9f059e | -12.05152 | -45.33277 | 2026-04-22 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45a8faa7-e0f8-3bdf-80bc-8b5233781215 | -21.71306 | -48.42349 | 2026-04-22 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e82c483c-c8c0-334b-912b-e5179d2e8c4e | -21.53508 | -48.89701 | 2026-04-22 04:17:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 39afe8a6-ba54-371c-ab24-f61f0da99187 | -13.63377 | -44.44344 | 2026-04-22 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4e95cfbf-d910-365f-8c7e-4e6c075b4ec4 | -12.02083 | -45.22866 | 2026-04-22 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36f4af96-ac6d-365c-9aaf-11dee2adac1a | -12.50308 | -54.76426 | 2026-04-22 04:17:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c25426b5-23ea-3b4e-b5c1-b4e20e8964f1 | -13.50458 | -47.49833 | 2026-04-22 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77e14ba6-f6d6-3199-bbb1-e984809b1207 | -13.38755 | -45.34047 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e50fbb0b-245d-380c-86ed-ccc2642c33b4 | -13.38593 | -45.32921 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e9d35f5-c767-3843-be9e-63ff532fe1a8 | -12.23615 | -44.18468 | 2026-04-22 04:17:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcc86c1c-6327-360e-9b4c-84200d059433 | -13.38811 | -45.3369 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a566ac93-4e68-387a-96b9-807f6bccc55b | -11.91152 | -43.84428 | 2026-04-22 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3529f376-ea5f-3183-b692-7b73cfe935f4 | -14.49766 | -47.76915 | 2026-04-22 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d97fb17b-3a19-306f-a937-37ffff46d672 | -11.77458 | -43.65252 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb973c2c-3911-3a6c-bfa3-f0a627ae5da9 | -11.77403 | -43.65606 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 14403963-badc-368c-8caa-c7d5705585da | -21.53093 | -48.90045 | 2026-04-22 04:17:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb24ff4c-fee1-3746-988d-514ad188dc9a | -11.9734 | -43.83968 | 2026-04-22 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bab60a1-6a58-3ccf-8a9e-e1ddeb2608d0 | -11.7674 | -43.655 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2d0ce148-9cf7-3666-b004-39a5e11b29e2 | -11.61241 | -47.10345 | 2026-04-22 04:17:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3a42182-aa58-36eb-856d-5fb2f0e86217 | -11.76794 | -43.65147 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3608475b-cbe7-3c9e-8d49-31448604a4ed | -11.77735 | -43.65659 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1afbc6e3-78ca-37a0-8a2d-5c323857c0c0 | -12.01026 | -45.2306 | 2026-04-22 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98d0be18-ed3a-301b-9e22-3a120c1232a2 | -13.37871 | -45.33168 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4f72ceb-27a7-3705-8af2-31e6c67ebf24 | -11.90821 | -43.84375 | 2026-04-22 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11fb666b-4a12-3ca2-9226-493666b903aa | -13.3809 | -45.33937 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f56a4685-94bd-3bf1-9764-a939bb1630e8 | -20.1575 | -50.98751 | 2026-04-22 04:17:00 | NOAA-21 | RUBINÉIA | SÃO PAULO | Brasil | 3544509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1abcc43a-6b22-30bd-99eb-3926bef1abd4 | -21.47002 | -48.65683 | 2026-04-22 04:17:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| da921212-5359-3a84-917c-b06b74295ab6 | -13.21325 | -43.68832 | 2026-04-22 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca4844d7-ebf4-3483-9acd-57fb491c46a9 | -11.99799 | -47.77482 | 2026-04-22 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a49c601-db5a-317e-8948-a35f42f2f315 | -20.86041 | -48.61786 | 2026-04-22 04:17:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d482bd7f-0695-3181-b311-c14612f8e14a | -13.28462 | -40.34673 | 2026-04-22 04:17:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2c994f3e-17cb-3645-b742-c34da9ad1b6d | -11.77566 | -43.64547 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e48808fb-dc2d-3f15-93bf-281f5344edc7 | -13.20993 | -43.68779 | 2026-04-22 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e8065cf-9332-306e-8762-e435eb9c5df0 | -14.90828 | -42.39711 | 2026-04-22 04:17:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f3fd9396-cabc-3fcf-93dc-6ccd523bbcde | -13.38204 | -45.33223 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70934ccf-13a5-3920-b784-42ea230f2328 | -11.77789 | -43.65305 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b5688cc-733c-379a-beea-5ff897c753b3 | -11.97671 | -43.84021 | 2026-04-22 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71040013-b65f-3879-9fe2-5fe5fe465541 | -12.28564 | -44.62856 | 2026-04-22 04:17:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5f1e737-3af4-39d2-8dbf-4e3754823a87 | -12.02473 | -45.22564 | 2026-04-22 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 479fc998-7683-3d3e-ad54-efe3e4f9c0d7 | -14.50119 | -47.76988 | 2026-04-22 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c822b167-4575-3574-b1fd-245bf0fa1e3c | -20.86385 | -48.61853 | 2026-04-22 04:17:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c5aa8f4-7587-34ce-9f19-d950e854eb50 | -11.76463 | -43.65094 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26657efa-62cc-3460-8ca5-9366f2abe5e7 | -11.99579 | -47.7655 | 2026-04-22 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e55ab1e-c18c-3f43-a343-263a413bdf64 | -11.77126 | -43.652 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 28500381-1646-3cfc-8fec-a5667443314d | -13.44567 | -43.79083 | 2026-04-22 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41e9bc0e-5461-34f8-a553-955c31d8f95b | -19.37485 | -50.91018 | 2026-04-22 04:17:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c9e25e1f-5b0a-34de-a1cf-fdbbfd4fc66d | -12.85295 | -43.77732 | 2026-04-22 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dc76514-94db-366b-b9f7-a82dcaa7569d | -14.90563 | -45.18285 | 2026-04-22 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc1ece5a-0916-3ebd-a783-3c9f1231c57c | -21.70901 | -48.42672 | 2026-04-22 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f1206c73-92e6-3f6f-a53a-97b8e95fccba | -12.24497 | -44.19329 | 2026-04-22 04:17:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f5f7a25-4fdb-35c5-9474-b76b55cf5bee | -11.77512 | -43.64899 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1e3afa2-f588-37fb-a40b-42030e0fd368 | -12.02139 | -45.22509 | 2026-04-22 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3f444dc-62b7-3c7b-8c26-20f6243e8e9e | -13.85005 | -41.41156 | 2026-04-22 04:17:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9220b5f2-919d-35cd-8bbf-d8fdcdf8da61 | -21.53162 | -48.89635 | 2026-04-22 04:17:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 219ad846-65fd-37da-93a2-573e7ad8f682 | -21.53439 | -48.90111 | 2026-04-22 04:17:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af852338-2a1b-3a65-b898-efa0988057f5 | -21.70966 | -48.42282 | 2026-04-22 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b6129497-7678-31e8-a139-7d4e62a8504c | -13.38868 | -45.33333 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22faee16-88aa-37b9-9539-a0a99b14c2ba | -11.99872 | -47.77047 | 2026-04-22 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c28ffb2d-d7ab-35ac-9e73-9e2d74b98f92 | -11.61323 | -47.10397 | 2026-04-22 04:17:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9626fd3-a988-3e3b-8e2f-21b7ccc836cf | -11.54282 | -38.98558 | 2026-04-22 04:17:00 | NOAA-21 | TEOFILÂNDIA | BAHIA | Brasil | 2931509 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d485e3b2-ca6e-36c3-af72-a4c4826a455e | -21.7124 | -48.4274 | 2026-04-22 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bb058521-11e7-3a3c-89f7-d565dd55ea79 | -13.38422 | -45.33992 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebb700cb-4d37-3c46-8379-0a232b7b35a5 | -13.38925 | -45.32976 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a26a0457-2bff-3c2f-a956-c0929cf19160 | -18.42685 | -49.59992 | 2026-04-22 04:17:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 884c8a9b-d9be-3638-a435-a8157054c24d | -11.91206 | -43.84076 | 2026-04-22 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0d957e2-95db-3704-ade2-583b2a2e20aa | -18.40731 | -51.43469 | 2026-04-22 04:17:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c793757-811d-3f93-b166-ea1688e27de8 | -11.90766 | -43.84727 | 2026-04-22 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6b3ce43-444b-3ec1-883c-b42ec69155fe | -18.43055 | -49.60063 | 2026-04-22 04:17:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| d7e140c0-2e27-3dfa-9b31-9ccd3b8c2f71 | -13.34747 | -43.20206 | 2026-04-22 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7742ba44-b451-3741-83a9-cf567977567f | -11.77234 | -43.64494 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4587959-8faf-3288-970f-141c7e76f173 | -11.7718 | -43.64847 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fa7e99dc-17c7-3eec-a99a-e80f3420869b | -28.1734 | -50.05857 | 2026-04-22 04:19:00 | NOAA-21 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 82c03aa8-b875-30b8-a38a-3ef05ccb367d | -17.16634 | -46.83305 | 2026-04-22 04:19:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 36a8c758-892f-365b-9f1f-573d09193c6f | -16.88842 | -40.62504 | 2026-04-22 04:19:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e90f638d-49ab-3be6-a054-045d6bb94f4a | -23.56465 | -51.73211 | 2026-04-22 04:19:00 | NOAA-21 | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1de6cadb-d86f-395c-9032-d1e80892f0cc | -25.26338 | -49.28031 | 2026-04-22 04:19:00 | NOAA-21 | ALMIRANTE TAMANDARÉ | PARANÁ | Brasil | 4100400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 539b2f28-4b56-339c-afa1-34db599b6a63 | -27.95443 | -51.06696 | 2026-04-22 04:19:00 | NOAA-21 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4a97150f-1715-3e20-991c-0646f4cc8378 | -28.47077 | -51.74842 | 2026-04-22 04:19:00 | NOAA-21 | SÃO JORGE | RIO GRANDE DO SUL | Brasil | 4318440 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
