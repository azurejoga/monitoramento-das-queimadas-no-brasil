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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03c0c81e-b21d-3849-a863-3c77569a7dbc | -11.17409 | -42.82526 | 2026-09-16 03:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 912d6b1a-e942-39e7-9651-d679177469ab | -16.2541 | -40.31734 | 2026-09-16 03:19:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 25a5bc67-6c9a-3707-b4d3-cb4540adf66d | -11.17444 | -42.7897 | 2026-09-16 03:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 30f133df-4f35-3d7f-a400-121cf4ca81d7 | -15.02846 | -41.46144 | 2026-09-16 03:19:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b8d4a4e0-2b45-3e87-9a61-0af1ce22ef4a | -15.8852 | -40.22557 | 2026-09-16 03:19:00 | NOAA-21 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 5aab7da8-53ad-3123-af20-bfea60105746 | -17.04403 | -41.28857 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| e1c3a3ba-32e2-34f7-b268-7131179860bd | -14.61012 | -42.14507 | 2026-09-16 03:19:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dbf80135-5435-3937-b31b-54466a59fd8e | -15.28579 | -42.80957 | 2026-09-16 03:19:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 006c8aa2-c42c-32bb-b6a8-56b4d802f411 | -13.55183 | -43.50728 | 2026-09-16 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 827ca186-2463-3271-99a8-cb71eba00a81 | -14.60419 | -42.14389 | 2026-09-16 03:19:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8d482a77-9641-3387-9ef6-b353551ea5eb | -11.83061 | -37.57418 | 2026-09-16 03:19:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| a8a33b97-e86a-3272-a620-874835f08f2b | -11.13066 | -40.47999 | 2026-09-16 03:19:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e2d6eb5a-9210-3e31-906e-b801c2e70904 | -13.55478 | -43.52593 | 2026-09-16 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2dee4189-444d-3e2b-a090-5fcc3cec45b8 | -14.69485 | -40.14015 | 2026-09-16 03:19:00 | NOAA-21 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 36888d22-f90d-3b73-b6de-75f424fa9651 | -11.20514 | -42.83308 | 2026-09-16 03:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d79fcebe-cb46-3a8d-8d85-a903a2b1078c | -15.88583 | -40.22244 | 2026-09-16 03:19:00 | NOAA-21 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f7f29713-bd37-3f5b-8fef-bcfb4cb8e5ac | -15.89034 | -40.22661 | 2026-09-16 03:19:00 | NOAA-21 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| ceffcab0-6d62-31ae-835d-76c7143b22e5 | -14.60915 | -42.14967 | 2026-09-16 03:19:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 72a745db-18bd-3eca-9eea-70fbe9b01735 | -17.03796 | -41.2908 | 2026-09-16 03:19:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 4600d86d-9d97-3653-9f6f-036815fb05ff | -17.0402 | -41.29525 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 0c2f2574-288a-36c6-9601-3446d149cadc | -12.71694 | -43.2071 | 2026-09-16 03:19:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 60139ce0-8ec6-3c9b-9912-cd0a6f6e9683 | -11.89257 | -43.83422 | 2026-09-16 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| bc632b0b-8b4b-339f-8d24-ca4f1ddd4e9b | -15.89379 | -40.23608 | 2026-09-16 03:19:00 | NOAA-21 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 036fd132-b491-3460-8c4d-3f95c6718300 | -16.78504 | -39.46193 | 2026-09-16 03:19:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 774511c5-1318-3a4b-86ab-5bbaeeeb9088 | -15.88096 | -39.93908 | 2026-09-16 03:19:00 | NOAA-21 | ITAPEBI | BAHIA | Brasil | 2916302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 945d882c-985a-3f9c-a965-f7c47f7afcd3 | -17.03639 | -41.28642 | 2026-09-16 03:19:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 26d3dbf5-3080-3aa4-84c4-3e140152a07b | -17.03953 | -41.28333 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5a5b41cb-0aa0-3e3b-889a-039b35b5785a | -12.47565 | -41.41483 | 2026-09-16 03:19:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b8d654ce-e0ca-3e7d-a815-164b5be6c83c | -11.88709 | -43.82495 | 2026-09-16 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 29326bd4-03ff-397f-8501-feaea043ab1d | -11.13234 | -40.4813 | 2026-09-16 03:19:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 89e29603-72a3-350a-8856-d9c6673a4723 | -17.03421 | -41.28198 | 2026-09-16 03:19:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 4fb4010d-6692-3541-bb49-0a2e5882593a | -15.36437 | -42.19983 | 2026-09-16 03:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 47565368-7eef-3fe2-912e-7698fb63411e | -15.28012 | -42.80631 | 2026-09-16 03:19:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7d5e8ea4-504e-3625-9203-d02f3d49f2f8 | -13.55323 | -43.52679 | 2026-09-16 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7de2469c-4f6f-356c-a043-37077319d247 | -18.2291 | -41.25487 | 2026-09-16 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c5db860d-774b-3d98-8d7c-04d2917a9683 | -17.04169 | -41.28788 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 78e22bce-896b-3230-bd09-af6b773f46ff | -13.55977 | -43.52822 | 2026-09-16 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a9f8c527-d3a5-3c0b-84cf-cf2282c7092a | -12.46667 | -41.39821 | 2026-09-16 03:19:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 00741e9f-4be6-38d8-b9f1-c099b83f5caa | -17.04031 | -41.27964 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2147ab17-1923-3804-abef-9b22fab5cb31 | -16.25467 | -40.31456 | 2026-09-16 03:19:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f303d4e8-416b-3184-a56a-5ef948e52b8b | -11.14117 | -40.4868 | 2026-09-16 03:19:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| dfca0016-6e91-318f-878a-19ce820ca0cc | -17.03499 | -41.27829 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 540b5ef2-faa6-351a-b48c-e05bbb9c1603 | -11.20026 | -42.83061 | 2026-09-16 03:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b930f18d-7382-3cd2-ad62-a194940437e6 | -11.88842 | -43.81844 | 2026-09-16 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 52882d4f-993a-3dc7-b14e-4f2c0e65ed6e | -12.47052 | -41.4006 | 2026-09-16 03:19:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 4e2ea51d-1bfe-365e-b34d-94266fdf62ab | -15.2745 | -42.8028 | 2026-09-16 03:19:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cb5b4d87-eba8-3b8a-8c6c-2334f95462c7 | -12.47267 | -41.3988 | 2026-09-16 03:19:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b327348c-9dab-3a78-ae79-60b569275081 | -11.14351 | -40.48448 | 2026-09-16 03:19:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| a5b088d7-1b95-343d-9173-d127822586ae | -13.55692 | -43.50963 | 2026-09-16 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 300928c9-95f9-3693-b79d-5a21c5fa9ace | -12.7181 | -43.20617 | 2026-09-16 03:19:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 858063cb-208c-32e9-9fad-404c861be6e1 | -11.83151 | -37.56924 | 2026-09-16 03:19:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 6593e45e-957f-3bfc-ade0-069bb9d6657c | -11.13709 | -40.47717 | 2026-09-16 03:19:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| efea1d11-ac84-3262-b5de-07df14270da4 | -15.2811 | -42.80164 | 2026-09-16 03:19:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| da8836cb-f246-3369-830d-168ca39cbfd9 | -17.04327 | -41.29222 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| dfb6bd77-7f64-3cfb-9043-3dcac1f7798c | -18.22527 | -41.24691 | 2026-09-16 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 52191a56-93c8-356f-8392-5ddfaadc47a8 | -16.25245 | -40.31575 | 2026-09-16 03:19:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 92c77ab6-da6d-30f4-a028-5c5977974cb7 | -11.88572 | -43.83282 | 2026-09-16 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f39fb33f-41c1-3506-ad77-d39d2660ead6 | -11.89395 | -43.82766 | 2026-09-16 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| eaad2a28-16c3-3cb5-a21a-3aaf5ac50bc1 | -11.24331 | -43.47491 | 2026-09-16 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0fd5bf80-869d-345d-a1d0-cc22b64e4f57 | -12.47255 | -41.42081 | 2026-09-16 03:19:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3f90b652-2384-3f99-a3a4-ede27ac0a7f9 | -15.89095 | -40.22354 | 2026-09-16 03:19:00 | NOAA-21 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| bd480d48-1b8c-370e-b2ec-f83b0f6eab94 | -13.56012 | -43.53312 | 2026-09-16 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 859719ed-5092-3bc8-a78d-bef3a5aee2bb | -15.2791 | -42.81112 | 2026-09-16 03:19:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 21feac4f-4c8d-3d60-8a92-90d227707042 | -18.2306 | -41.24759 | 2026-09-16 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 276be752-4575-36c2-a0a9-bba61e325aa6 | -11.24971 | -43.44366 | 2026-09-16 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 387ed22c-31c4-33b9-bd1e-09f5aaec49d8 | -11.16447 | -42.80544 | 2026-09-16 03:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 15c09c49-51a1-3650-ad32-69e6c4a30c09 | -11.16986 | -42.81246 | 2026-09-16 03:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e4e8d161-8d5a-3c3c-8e93-d33598254402 | -15.89435 | -40.23327 | 2026-09-16 03:19:00 | NOAA-21 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 403952dc-733f-3bca-ba7b-348b8ff9a9dd | -11.13559 | -40.48511 | 2026-09-16 03:19:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 91b8c509-e612-32c8-a9e1-cb0f1bd1f4fe | -18.22452 | -41.25051 | 2026-09-16 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8dc13fc2-1b56-39de-af59-4f4bc2ebb280 | -11.8871 | -43.82628 | 2026-09-16 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 68fe5268-6715-3123-8cf9-b113875fc777 | -11.20097 | -42.82024 | 2026-09-16 03:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d8b2b517-43c6-3cb5-98fc-89ce184855fc | -11.19718 | -42.81192 | 2026-09-16 03:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 8b18377d-d136-34a4-ac37-eb6758f39922 | -11.19562 | -42.81321 | 2026-09-16 03:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d7ce40a7-1195-3222-992f-77eb519a3c54 | -11.14192 | -40.48282 | 2026-09-16 03:19:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| ed96152b-18b7-39b6-83b1-35c0a40134d9 | -15.29126 | -42.81382 | 2026-09-16 03:19:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0037ac15-321b-34b2-94d8-ce25c0e4f596 | -18.22729 | -41.23709 | 2026-09-16 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| ba12b635-11ea-3e9c-a6ee-87507ce421f2 | -17.04107 | -41.27604 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d78aa8de-d5a3-31c5-bdda-ced9da2aca3c | -11.88575 | -43.83151 | 2026-09-16 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 71288624-8ee6-333e-9d11-4bda7014d8c2 | -12.19653 | -43.47815 | 2026-09-16 03:19:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e481c0b0-2f3a-3aab-a7e2-fcc3e4f91018 | -12.47487 | -41.41882 | 2026-09-16 03:19:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 40be7945-beb9-372f-b77f-59c679dae93e | -12.47198 | -41.40233 | 2026-09-16 03:19:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| aeca0e9e-4b98-3f68-bfe7-59d59d8c656a | -11.1986 | -42.83175 | 2026-09-16 03:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 917c051e-35dd-3bdb-a55d-deac37521a22 | -11.13642 | -40.48075 | 2026-09-16 03:19:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| be282f68-781d-3145-8d59-f49982eb102e | -17.03874 | -41.28707 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| e47b793d-9fa3-3896-9ea4-219b174b3d4c | -17.04251 | -41.29584 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 6c6dc660-7ba5-3b3b-8563-7f067ec23251 | -11.89532 | -43.82114 | 2026-09-16 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| c4e27c15-9b7f-321a-afb6-7213ee0ce37d | -18.21994 | -41.24618 | 2026-09-16 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b4d8e8bc-97ed-370e-8a71-a92d3218eef7 | -11.24201 | -43.48124 | 2026-09-16 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 652979fe-3ba4-38d0-9276-63be677c17d5 | -17.03792 | -41.27891 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a46c62d7-c056-3181-b073-3a15f83d84eb | -11.19978 | -42.82601 | 2026-09-16 03:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 299c3762-8a79-3eee-9dc4-90fe0f61c289 | -11.13803 | -40.48237 | 2026-09-16 03:19:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 2c54ceb1-002e-38b6-9d9e-67ad886fd192 | -9.112 | -45.7294 | 2026-09-16 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 8533c533-859c-31c9-9d70-b90097e6109c | -9.0931 | -45.7314 | 2026-09-16 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 739f49c6-831d-32e0-81a9-ecd7f39f0379 | -5.1215 | -47.6146 | 2026-09-16 03:20:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 0c38c23b-49b1-3047-93e4-c41a83e61209 | -12.7521 | -51.2213 | 2026-09-16 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 272b685d-4de3-3c0e-8da9-1851de610974 | -2.6966 | -57.6084 | 2026-09-16 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 21515445-5507-3f2b-9ce5-fbffaa090423 | -11.1401 | -40.4748 | 2026-09-16 03:20:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 76.5 |
| ab37d9e1-d2b3-33f6-8400-84d7f9f277ac | -12.7709 | -51.2403 | 2026-09-16 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 8c3973c8-d725-3ebb-94ff-92ffac28069f | -12.7901 | -51.238 | 2026-09-16 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |


[Clique aqui para ver as próximas entradas](README13.md)
