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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95cc0118-5994-355d-bf50-48cf3c3e7ca4 | -11.44733 | -43.4441 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e45dd0ed-27a0-3f18-ab2c-6327848d9a77 | -11.12768 | -44.5901 | 2026-10-01 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbd020b7-6a54-3c98-a708-df2e9790c900 | -10.8541 | -48.68332 | 2026-10-01 03:38:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1fe6ad98-296b-37dc-bb76-16813d6caa41 | -7.57317 | -46.62383 | 2026-10-01 03:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cee0d505-fb56-321a-b586-fe23b661c45a | -12.35475 | -46.3806 | 2026-10-01 03:38:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cebbf9a7-3d0c-3a43-af05-c6f64e7e792a | -8.04707 | -42.86484 | 2026-10-01 03:38:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5828e021-991e-3159-8c05-94be824119ca | -12.85759 | -44.33727 | 2026-10-01 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9fd5d5b3-a359-39be-9c71-1c69a08ef181 | -8.96653 | -44.17873 | 2026-10-01 03:38:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97d66bd5-01bf-3fc5-80a3-75bda9236887 | -9.20769 | -45.8226 | 2026-10-01 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 087141fd-8a48-3f9e-95d7-3abdead47edd | -11.43727 | -43.41463 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0632de5b-e690-35c7-89c9-bf0bdf9987f5 | -9.79291 | -44.81179 | 2026-10-01 03:38:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa9e095d-1d5d-3226-9936-8e17722627fb | -11.37998 | -43.36185 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 085c1b87-dc1d-3c3f-9229-29d35633c972 | -14.36876 | -44.77579 | 2026-10-01 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dc0ef88-25b2-360b-b56b-d135d41fbd96 | -12.64383 | -47.63634 | 2026-10-01 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| be47a311-d577-3a00-8c61-3a1263c95892 | -11.34497 | -43.35519 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97f8d40f-9d81-3a5b-ae1e-1adbd3b278cc | -15.63817 | -40.99252 | 2026-10-01 03:38:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 81b36e03-e65c-3e54-b7db-f9a660c1027b | -8.21069 | -46.20208 | 2026-10-01 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 14313fe4-8e69-3ad2-9080-351b049b3c2a | -15.64215 | -40.99324 | 2026-10-01 03:38:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 93d76b38-5f6c-335d-b32d-53dc3affedf9 | -11.45626 | -43.45199 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38f3e5d3-5bfc-3fca-8609-63cd0064af88 | -11.46129 | -43.45295 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8570827e-9b66-3d5e-ae3f-1e62b71cb872 | -10.32988 | -47.78725 | 2026-10-01 03:38:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b17d5af-c845-344c-a68a-35ab4ceef70b | -11.34943 | -43.35907 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0357c80-ba82-3962-bc5e-cc451316fa80 | -11.44564 | -43.42538 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| af2f9150-5ee6-3270-acc3-a9b902bf2fbd | -11.19111 | -45.19083 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8af24c4e-ec79-3e22-a04c-466d940151ca | -14.37397 | -44.77678 | 2026-10-01 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 40c9cb00-83bc-383b-adeb-37e848dfad86 | -9.75669 | -44.81741 | 2026-10-01 03:38:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bc38f6e-035f-33c8-82dd-180d87b8bdd0 | -13.38225 | -46.81489 | 2026-10-01 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fb4c539c-056b-38e1-92a0-6aaefa9a1851 | -8.04248 | -42.86098 | 2026-10-01 03:38:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5541eb9c-8168-34c3-aa03-401fe23a725b | -11.6207 | -43.53815 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa95ebc7-2309-36b0-a88e-fd7e8ec0abfb | -13.38518 | -44.02525 | 2026-10-01 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed4038c0-5d96-39fd-8d4e-af34e24e8d11 | -11.41331 | -43.40403 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4839099f-e4d5-3d95-93a2-f19ed4686048 | -13.38474 | -46.8333 | 2026-10-01 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7aedd46-a912-3552-9e5c-90c3d6ed91bb | -13.88243 | -44.45527 | 2026-10-01 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 17027467-d83f-3738-9506-d68faed2814b | -11.61786 | -43.55313 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f62b3d80-8dcb-3229-a2c9-e4c4a036b34a | -9.20237 | -45.81735 | 2026-10-01 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b614993-26c9-3cbb-a168-176dff815e95 | -13.38307 | -46.81092 | 2026-10-01 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d03129f8-f631-37de-b511-b2274b15ba9d | -11.41381 | -43.48377 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fe81767-e104-3ce8-b169-a7e091403ba3 | -8.2088 | -45.47278 | 2026-10-01 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59150a59-31d3-3995-b146-75abebb4dbd7 | -8.84623 | -44.39406 | 2026-10-01 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcbce6e8-13ad-383b-95a6-54d6c1cfe8cd | -11.68499 | -43.50096 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6852354d-1579-3ae8-b6ab-89e0f86ec65d | -8.13125 | -43.5281 | 2026-10-01 03:38:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18d78fb5-7b77-3a6f-b73a-31497082bece | -11.18172 | -45.11679 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4be9bf4e-e944-3940-82db-0767dd64afa1 | -11.40258 | -43.48792 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97abac00-9c8a-3e9b-a7be-12c7bdd99ee7 | -12.18443 | -47.38291 | 2026-10-01 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a9723fbb-5db3-31f0-98e1-1bb2538be2ef | -11.38851 | -43.39996 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36a9a6cb-4a9d-33d2-bace-bf90e3ea37ca | -10.29747 | -44.6434 | 2026-10-01 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78f1f38e-7fc5-316b-895b-33bd6fffe440 | -11.4075 | -43.40962 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5145925f-e62f-3728-80d8-03e6a818ec18 | -7.60972 | -44.55606 | 2026-10-01 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 395ab969-2f79-3c64-9031-4cee7d3dbb05 | -8.20338 | -45.50238 | 2026-10-01 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3107f27e-a727-3d27-af42-aaeb1f702590 | -11.44844 | -43.43817 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aaa63a78-3d82-3dba-8a2c-86714b48dfa3 | -11.2626 | -43.52337 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f03a130f-79cc-3a02-8909-db7a690b4b87 | -11.20685 | -45.15328 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0efed37b-2ddc-395f-8d90-5e423bb81b49 | -12.41308 | -40.92466 | 2026-10-01 03:38:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9b97433d-3be6-3cc6-86be-dccd49ef7bb3 | -10.84848 | -48.71054 | 2026-10-01 03:38:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| de3d2a64-a847-33bb-bf37-ff584a716c52 | -9.5723 | -37.3823 | 2026-10-01 03:38:00 | NOAA-21 | SÃO JOSÉ DA TAPERA | ALAGOAS | Brasil | 2708402 | 27 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4d6c6b45-c6fd-3088-84db-0400d720d5cd | -8.84688 | -44.39063 | 2026-10-01 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d46ac8b-6e3c-3869-8475-3b28cac0998b | -10.85283 | -48.68949 | 2026-10-01 03:38:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 71378e6b-5414-3295-9af6-b55c9b8d4775 | -11.41162 | -43.4129 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 691b1ac0-98cf-3af0-93e3-9dbffe80f53d | -10.32308 | -47.78638 | 2026-10-01 03:38:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8611d57a-765c-33e5-ac84-ec17c0bd32ac | -11.41324 | -43.48677 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 122f8607-5dfb-3629-85f2-97ef6beeac56 | -12.64271 | -47.64186 | 2026-10-01 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eedf27f3-37c1-3b73-a377-cf4185a4fdc6 | -11.127 | -44.59365 | 2026-10-01 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea1ee6e9-a065-360f-937b-7957bf88f25f | -8.84861 | -44.39138 | 2026-10-01 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2d40cc7c-c74e-3ff0-aefd-df3f8a76389d | -10.29527 | -44.65025 | 2026-10-01 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92cf3166-da14-3f24-b9a7-145e17bc20e2 | -11.41251 | -43.41059 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94321591-c522-3c91-ba0b-3c5b4036a49e | -13.38737 | -46.82045 | 2026-10-01 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 611675b1-4d59-366b-8a79-f293dd70ebde | -12.56361 | -43.07655 | 2026-10-01 03:38:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| cbb015b3-4cda-34fe-b253-41ae38744d92 | -11.47024 | -43.46077 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf7799b7-1c18-3e0c-8fa9-e51fa639143b | -11.18942 | -45.10693 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ff8e63b-4627-33f5-aedf-bf37f12b001a | -12.19552 | -48.43405 | 2026-10-01 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| f4f64447-0734-386f-87ce-9a275b126bf2 | -7.5048 | -45.83184 | 2026-10-01 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a809ead3-8651-35bb-ae46-e6af1b62be81 | -11.40661 | -43.41195 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a27e73e8-2fc7-3fba-b1c2-ac0697fe6b42 | -11.20347 | -45.20064 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d1540b5-67df-3947-aa31-c1a3a0ba2997 | -11.42834 | -43.4069 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ff7879cb-b4f4-37b4-b54f-cc5e5006d78c | -8.04538 | -42.86059 | 2026-10-01 03:38:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c7dde507-6d4e-35fc-bf68-21a399539fb5 | -11.43951 | -43.43036 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6b84d65-a7d6-3023-b11b-eeafeb9b0db9 | -11.43515 | -43.50917 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a232909-ad52-352b-bced-e209d3285b7c | -11.18808 | -45.11403 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0e52b2f-649b-3e59-8daf-a98db72f0304 | -13.88758 | -44.45625 | 2026-10-01 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8c07cb4-36d4-3c91-8585-2650d563e216 | -7.38221 | -46.42989 | 2026-10-01 03:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c5e72b64-05cf-35ef-ac97-48a7f9a5e16e | -11.42277 | -43.40892 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 81bfe813-38ac-3cc2-a073-5a0e495c14b3 | -14.3681 | -44.77919 | 2026-10-01 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74aaa798-5343-34f9-aeab-e08ec55fd533 | -12.8622 | -44.33744 | 2026-10-01 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 93f5b464-4c6c-3894-8606-26fae7d420c8 | -8.29381 | -46.74813 | 2026-10-01 03:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1a7bca81-f753-372a-ab96-f9d0a9cfdf94 | -8.96721 | -44.17502 | 2026-10-01 03:38:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22b54878-d097-3f91-8e0d-2a1e1959ba30 | -11.26823 | -43.52127 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2b1c270-acf4-31c8-9906-30b05ec7b454 | -11.66129 | -41.84394 | 2026-10-01 03:38:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bc1c78b8-49e5-3e64-9766-a65b21110ad1 | -11.36107 | -43.35216 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f8517d6-2926-3b2a-be42-23ecee94e457 | -11.21239 | -45.15484 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ac1f2c2-7ff5-3516-990a-48a477c38ee0 | -8.64114 | -45.29534 | 2026-10-01 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60c94ae2-5050-3157-8735-e6609ad6cf3c | -11.40315 | -43.48492 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca9206c6-cf92-320e-ae72-ed55686a9313 | -12.18746 | -48.43891 | 2026-10-01 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 00a495ad-b37e-3c2e-b25f-587f8ca33b59 | -14.55326 | -42.7424 | 2026-10-01 03:38:00 | NOAA-21 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5e28a4d0-22a4-368f-9231-0ce35d74f7d3 | -13.87261 | -43.99538 | 2026-10-01 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c197c023-61eb-35c8-8763-2a2cf1dafbcb | -8.33171 | -44.16312 | 2026-10-01 03:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6f79460a-0846-3c69-ab3b-678794abc40a | -12.56452 | -43.07151 | 2026-10-01 03:38:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e2d910d2-b5f3-379e-8fc8-4564ee9e2c48 | -7.85082 | -45.8316 | 2026-10-01 03:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e881da2b-751e-3e6a-9823-e276fa9d02a4 | -11.19361 | -45.11562 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afffe149-027b-35f9-ba79-f76e6e84128d | -11.19367 | -45.19075 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 52f1913b-7042-388b-891c-e14cc84d59a8 | -14.23637 | -44.22997 | 2026-10-01 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
