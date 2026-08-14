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
| 82becde2-2978-3362-8bd4-6ec50cddb251 | -6.98012 | -41.46993 | 2026-08-14 03:36:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6a49b8ed-5167-3e19-8058-8c603bfd7961 | -7.02859 | -41.4469 | 2026-08-14 03:36:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 228af2d4-5fb0-3e9a-8e07-a21b7d25b8e6 | -6.84403 | -42.90511 | 2026-08-14 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d1bfe5b6-9205-3288-b023-7721f1977e15 | -4.5062 | -42.54126 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 8397d0a3-1cb6-3d5e-8c07-73c0bc368cde | -6.91527 | -43.63485 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ab6ea514-b2a4-309d-83c4-747f032fafc3 | -4.50449 | -42.5515 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 567468cd-8deb-3dc6-a90f-5ba386ba457f | -6.11211 | -44.02654 | 2026-08-14 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 65805307-8b77-3e85-82d1-5644d3ff980f | -6.11246 | -44.02745 | 2026-08-14 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5ca7eaf2-3664-3571-b2dd-340e89391ea3 | -6.909 | -43.63779 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e60be69d-1650-3db9-ab96-a4bffaaca8fb | -6.25853 | -43.27611 | 2026-08-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 834fdd11-ff2c-3916-a1df-a2a892fc10a8 | -6.91077 | -43.63414 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2d625be2-0885-307c-bf2a-fd3dc33fe4e2 | -4.51043 | -42.54908 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6153f4f1-86e8-333e-b5a3-515692fe2774 | -6.9101 | -43.63796 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 42979a87-935f-388a-9d63-a646db775a4d | -7.02383 | -41.44595 | 2026-08-14 03:36:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 5df4ba90-955d-36d4-9032-56daccb2879e | -6.91567 | -43.63886 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b5d91699-557b-387a-8d9d-ec626c2b8439 | -4.49486 | -42.54295 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 4602c7a0-4934-35e7-90cd-de5b46e2c191 | -4.50563 | -42.54466 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9aaa94e2-b92a-352e-a28a-1739cd23f715 | -4.50677 | -42.53786 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| ab14fae2-7ede-3a9e-9dc4-f5065d9e9219 | -5.59444 | -37.73939 | 2026-08-14 03:36:00 | NOAA-21 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1e76bc67-14a4-3a14-bd71-454dc53c2348 | -4.511 | -42.54566 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b020663f-5085-36c7-9057-5dcef082e9ca | -6.92034 | -45.73642 | 2026-08-14 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 14730cfe-f089-3738-b3a9-c483d48f95ef | -6.26403 | -43.27697 | 2026-08-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 599c6de7-45be-3043-9c60-e58270f5716d | -4.49852 | -42.55405 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 068823fc-0228-32c3-abc3-b76d9d60be8f | -4.49197 | -42.56007 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ec63de0b-3f59-32cb-8cbe-d5f1107fcf88 | -4.49794 | -42.55751 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 81ccdd8a-329c-3c6a-84d7-921e18e19a6f | -4.49255 | -42.55664 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 15478859-0841-310a-b246-627544c54f71 | -2.90658 | -40.39207 | 2026-08-14 03:36:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c57a5b6c-5e6d-3662-b1d8-356cddde26bc | -6.26467 | -43.27337 | 2026-08-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 789590d7-bca0-3842-9680-866219c5d447 | -6.91945 | -43.6434 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4b3be8a4-e9af-319c-bdde-c7a1cf575431 | -7.0031 | -44.83036 | 2026-08-14 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 541b5f0d-3f74-33c7-a255-a6c5f5073555 | -6.915 | -43.64266 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7ae6e843-2fbf-3e60-a44a-1d2684f6c03b | -4.50139 | -42.53696 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 0e48b70b-8530-3af4-b63d-6048ab78c0ad | -6.99714 | -44.82917 | 2026-08-14 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 61a0c529-09a6-3137-ad23-67e06b7d7a59 | -4.48715 | -42.5558 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e0c2b318-5c41-3760-8f67-6c04999f3db2 | -6.26887 | -43.28159 | 2026-08-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57fac9a9-47ad-3016-a974-c008514e3bc1 | -4.50082 | -42.54038 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 89e45735-e498-3394-b6f6-8475a58d956f | -4.4937 | -42.54979 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 008ff965-132f-346b-974d-0f6d2d761df5 | -15.13797 | -41.5632 | 2026-08-14 03:38:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| a4230316-fee3-3ab7-9777-5068e3f9293c | -13.56156 | -46.25861 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 95bc4bd2-1ee9-3f39-97a4-098ead78411e | -13.55768 | -46.24791 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1035e0d8-ea0b-35bd-b3d1-728826f452be | -7.71425 | -46.23142 | 2026-08-14 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c448c932-9250-324e-9c43-d211669f0f04 | -13.74605 | -42.57323 | 2026-08-14 03:38:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c921d093-1299-3d24-887b-dc9433afbd5b | -15.13376 | -41.56245 | 2026-08-14 03:38:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| a0115e77-8dd4-34a8-b252-08805ba232f5 | -7.80749 | -44.11386 | 2026-08-14 03:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 110b9727-9294-3b47-ac1c-f8d0349d6906 | -14.47132 | -45.69626 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 468ef74f-aa42-3305-9599-1f3a1ad6592d | -7.45416 | -46.15067 | 2026-08-14 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40162cf4-8c01-3cdd-a71f-6808b0185791 | -14.46731 | -45.68753 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ad04179c-eafa-3b67-81fd-4d8eae608eeb | -14.24217 | -45.41473 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70f38c71-b026-37ce-ac47-c8a5a676fd0a | -12.49208 | -43.77659 | 2026-08-14 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 399fd448-43e9-3117-aee5-608cb2b9955e | -15.13724 | -41.56714 | 2026-08-14 03:38:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 017ab173-af93-39a6-9c9d-90f58063c60e | -14.45315 | -45.70033 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a38f94c-2c23-395b-82bc-cbc999bdda42 | -14.45392 | -45.69654 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b03a5ae4-ea66-3060-9f36-8f8979c31867 | -11.42979 | -43.91927 | 2026-08-14 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fc05ba7-030d-3081-b9e4-329c5f9cf343 | -7.80677 | -44.11788 | 2026-08-14 03:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5555d1d-63fc-30eb-af71-b4b8903b50d9 | -14.29552 | -45.26685 | 2026-08-14 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cee256bf-12be-331f-80d6-195d605e03bd | -14.45469 | -45.69277 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e2773e6-e2c7-39bb-966c-125581efd0f0 | -12.76138 | -44.55444 | 2026-08-14 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 987c76cc-a71e-32b2-8315-aaf8e4901443 | -12.02631 | -47.82443 | 2026-08-14 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 439c1496-9ddc-3b69-93d2-45b3e2656980 | -13.39304 | -42.38629 | 2026-08-14 03:38:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| a162520c-f6f1-3840-98e2-0b3495719e14 | -13.55625 | -46.26127 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| acfaef76-9989-3a09-a7e0-d964fde0e198 | -14.47208 | -45.69246 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f8a7d7af-bb63-3d4c-8967-88630251df12 | -11.88646 | -45.96053 | 2026-08-14 03:38:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 003eb172-f1a5-35c3-87f5-d8655ae4e99f | -13.56393 | -46.25322 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 401cb0f0-c36e-3baa-9252-0fc1cb433184 | -13.39216 | -42.39103 | 2026-08-14 03:38:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 2bc0ef3c-2657-3cf5-b9e8-f57fa1133b49 | -11.88439 | -45.95839 | 2026-08-14 03:38:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 473a9034-0ff5-3e09-b622-6caf933c4d17 | -11.32158 | -45.21972 | 2026-08-14 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cdaa514b-425a-3fa4-bc05-524207e734b6 | -12.02078 | -47.81813 | 2026-08-14 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fd62e3a9-b06c-3fe9-a711-420376f43cd8 | -13.563 | -46.25791 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0e42bb4e-4f7b-3c8b-81fc-48fe5bfa268c | -11.4829 | -45.0961 | 2026-08-14 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ea944d4-d749-31fb-a69c-c1f7ce2a5234 | -14.46654 | -45.69132 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5155a2c8-af02-3cac-af26-d83e742137b4 | -13.55715 | -46.25673 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5e419b37-4b8e-3800-97d2-d8ed5cc09f06 | -14.29942 | -45.26765 | 2026-08-14 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6858aa99-6c0d-3115-8e47-a97ef22e45a8 | -13.38846 | -42.38549 | 2026-08-14 03:38:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 561cd629-c7a0-3a4f-a8db-f2952b2da430 | -13.383 | -42.38945 | 2026-08-14 03:38:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| da001c76-a567-39d0-8c82-cd0a6bcbfad5 | -13.38212 | -42.39421 | 2026-08-14 03:38:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| aa25205d-15e7-3f68-a850-9fce1d927464 | -15.13943 | -41.55528 | 2026-08-14 03:38:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f244d5de-7008-3b56-8d34-d4a71796f9c4 | -14.47285 | -45.68866 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f20c1895-34b9-3911-9032-727acda459c5 | -11.88141 | -45.95496 | 2026-08-14 03:38:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b4dccf73-730d-3224-9bf6-bdf06715f216 | -13.55667 | -46.25279 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2705bf11-deb7-302e-8436-d519b2206d29 | -14.47686 | -45.6974 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1aed26d3-856f-3198-b694-2ebffb67817b | -12.01966 | -47.82343 | 2026-08-14 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 014d71ba-23ce-3296-b7e6-71e435cc452a | -7.70538 | -46.23977 | 2026-08-14 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a2f9d577-c45b-3673-9495-1411867ec615 | -13.55571 | -46.25744 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9784fc42-27ba-3730-ad9d-9bccf1868a4a | -11.45469 | -44.55856 | 2026-08-14 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3331f208-4f2a-317c-94b0-fa858c4c49e3 | -15.14218 | -41.56391 | 2026-08-14 03:38:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e0c9b46f-c134-38a0-89ac-fc5135622919 | -14.63244 | -42.51824 | 2026-08-14 03:38:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d3d90b9c-e5cd-30b2-a8b5-633cf2797fa3 | -13.56251 | -46.25397 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5f166176-7102-3c62-9216-7cfc6b514678 | -13.38758 | -42.39023 | 2026-08-14 03:38:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| b715425b-4677-3a92-be4b-575ec865c1d9 | -14.4476 | -45.69918 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fb08462-8a66-348c-aecb-a02a471f96ca | -14.44838 | -45.69539 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 560e43cb-d6ff-3aea-80e0-9990c90140a8 | -14.46808 | -45.68373 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8b30e7b0-31ad-3dca-910f-609288616374 | -7.70647 | -46.23393 | 2026-08-14 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e17c4bdb-b898-3f36-95d0-1ad3eee35d3c | -13.86048 | -43.64629 | 2026-08-14 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44766b42-eb82-3d75-860a-ba5818e9d4fa | -13.5621 | -46.26245 | 2026-08-14 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 017572b3-eec9-379e-bbd2-e3292a64a121 | -11.8835 | -45.9628 | 2026-08-14 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e026e2b7-b58c-31a9-9dcc-894f437e7bac | -12.49323 | -43.77048 | 2026-08-14 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5460b670-b391-39af-a7a5-bc0a58aa2148 | -15.53127 | -40.85397 | 2026-08-14 03:38:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ccf3162c-091b-313b-8292-d0f9f07f1604 | -14.4784 | -45.68979 | 2026-08-14 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f12edaa7-97d4-3554-8e18-366f8ebb057f | -12.71273 | -48.44015 | 2026-08-14 03:38:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 56835d6f-518a-33ec-9a56-bf4b42911b89 | -12.49381 | -43.76742 | 2026-08-14 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README9.md)
