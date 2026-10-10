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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6882b0a5-8398-3e6c-aa26-b350e6a06d7b | -12.037 | -43.429401 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9a27ea8d-166b-3e34-87db-6eee27d40117 | -11.4513 | -43.370399 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f3995076-b3c4-3c23-be34-7c9871aacca0 | -5.7352 | -45.124699 | 2026-10-10 00:09:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49d428ac-20c0-3685-8348-c46a848988f8 | -13.3782 | -43.8797 | 2026-10-10 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7bd8579-e955-3762-988f-06660d19e6df | -5.6972 | -41.749298 | 2026-10-10 00:09:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2f151e94-c070-3686-be9e-3d621ce38b5d | -5.7395 | -45.144001 | 2026-10-10 00:09:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3e4d0a5-19fc-30c1-b698-f05c5739d405 | -4.9006 | -43.461102 | 2026-10-10 00:09:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f6c82f7-c9f5-372e-b025-48af36c08043 | -3.7891 | -45.784599 | 2026-10-10 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a9072d65-de8c-3985-b75f-329c7ac7d59a | -4.5729 | -40.665298 | 2026-10-10 00:09:00 | METOP-C | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f7cc5078-a911-3c7d-b6b2-ad375bbf72c8 | -12.1151 | -43.3148 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80ed38f2-8546-335d-9c9d-d8bf9d570469 | -18.0797 | -42.2682 | 2026-10-10 00:09:00 | METOP-C | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f9850619-e482-3f8f-b1a4-4ca492b297f9 | -4.0232 | -40.652199 | 2026-10-10 00:09:00 | METOP-C | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6ee9a1fa-afe2-3b6f-b546-32889c4dcf88 | -13.163 | -43.2878 | 2026-10-10 00:09:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a19389ae-d16a-37e7-8d07-013f79a3237e | -11.5923 | -43.744202 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| adf31d80-5e93-3cfa-9eb8-c44ea6dddd6a | -12.3514 | -46.584599 | 2026-10-10 00:09:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 468a4f1c-1fd5-3f6e-88fc-87684e2a8f99 | -14.4424 | -40.731201 | 2026-10-10 00:09:00 | METOP-C | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 46db04a3-f6b0-3da8-9a97-0d20482ccb9c | -17.4492 | -45.089699 | 2026-10-10 00:09:00 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cb77db18-735b-3690-9c6f-2e826904f586 | -13.2533 | -44.015999 | 2026-10-10 00:09:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 865cf340-a1b6-3502-a537-b8c25eeef133 | -17.1381 | -41.3568 | 2026-10-10 00:09:00 | METOP-C | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd7daf21-270c-377e-b1a5-214b246918f1 | -4.3099 | -41.226799 | 2026-10-10 00:09:00 | METOP-C | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| afc573ef-3d3a-30d5-ab22-4e6007263ebf | -13.4465 | -43.618301 | 2026-10-10 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5091d9f7-2298-3387-92cd-0fff2ade5d58 | -3.7397 | -50.010101 | 2026-10-10 00:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecaa154e-4e51-3b06-842a-dc7727615b27 | -5.7493 | -45.141899 | 2026-10-10 00:09:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06e6032a-2c45-362a-98f7-b3e24a26eb57 | -11.6644 | -43.698502 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96d41942-b04d-3ac8-a0f6-66be0d3ceef2 | -4.5927 | -49.2173 | 2026-10-10 00:09:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d52bdcc-1d91-3660-87fb-5e3660366f3f | -14.4251 | -43.961399 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 71114aac-4f5e-3a98-8d0e-fadefe1ea773 | -11.5918 | -43.693901 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 122900ca-aff5-38bf-a0d8-6e0f80f5c1d1 | -9.5595 | -40.334099 | 2026-10-10 00:09:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 29000627-b58f-335e-a332-dfeae4f7f1a0 | -7.074 | -41.597 | 2026-10-10 00:09:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 374ff1e0-1ee5-38fc-ad73-ffcf4d5f8435 | -7.088 | -41.750099 | 2026-10-10 00:09:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b144d0c2-789d-3461-ab92-1684baeb7774 | -9.8399 | -48.000198 | 2026-10-10 00:09:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe9355f2-9493-30c9-90f6-918155288956 | -5.8884 | -43.416302 | 2026-10-10 00:09:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2e68d24-697e-3bf1-8660-d22e3267c965 | -6.4039 | -43.744801 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b587a62f-05ae-32ef-8336-fe06c62e8ab9 | -3.6779 | -47.805199 | 2026-10-10 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e999e590-482a-35db-9a3b-229b7be02b2c | -7.0994 | -41.755001 | 2026-10-10 00:09:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7498f0be-8154-364a-a17d-776be756a964 | -11.1168 | -43.243401 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74f9b965-8ddd-3748-8f3e-6d8b31cf5120 | -11.0692 | -44.123199 | 2026-10-10 00:09:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 69c57185-3142-340a-a646-5a1cc65f880a | -8.2482 | -46.420601 | 2026-10-10 00:09:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 127b98a9-6783-3d09-a282-3e495e332a8b | -8.2455 | -46.407902 | 2026-10-10 00:09:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6a1bf39-b9d9-3c27-b2f6-52adc7192161 | -6.7031 | -40.465698 | 2026-10-10 00:09:00 | METOP-C | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cff7be95-bc95-3a22-92c4-66de1550cf2d | -3.7522 | -45.940201 | 2026-10-10 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb51d968-0fce-37d6-ae46-e3c2508a8bbc | -4.3869 | -46.5312 | 2026-10-10 00:09:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| abc2d5e6-12ca-3eeb-89ed-2b60ef62fd5c | -16.651501 | -40.551899 | 2026-10-10 00:09:00 | METOP-C | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 847332bb-ee3d-35ad-a99b-56a4e917673a | -13.6316 | -44.418301 | 2026-10-10 00:09:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9de33735-3bcd-3bae-b252-eaa8ba5106c5 | -4.3844 | -46.519901 | 2026-10-10 00:09:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 634621fe-810b-3879-b9b2-fedfbab23e2b | -14.0132 | -48.757401 | 2026-10-10 00:09:00 | METOP-C | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d0ee3cbc-dd42-3854-afdb-8803313238d6 | -12.0448 | -43.4179 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 92224bbc-7a76-3a94-b029-d64463207db9 | -6.2026 | -45.429699 | 2026-10-10 00:09:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8cf4419-f312-353f-87a5-76d693366b48 | -11.4532 | -43.379601 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 259d6a2e-46b8-332d-aff0-a75fa81bb05c | -5.4518 | -44.7729 | 2026-10-10 00:09:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d6851fe-f736-3290-94d6-8c553de0d501 | -4.3892 | -43.1115 | 2026-10-10 00:09:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46889da0-0c9f-3153-ae96-140fb9cc01c1 | -15.3771 | -41.941601 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ed01db20-8ac8-31ed-a09d-f9ff25f6f948 | -7.1555 | -52.610802 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 621b18ea-53c9-361b-a1cb-1921c73a8cad | -5.9453 | -45.378899 | 2026-10-10 00:09:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75b142b0-6cbb-37c8-94e1-7fec26633400 | -11.0217 | -45.451599 | 2026-10-10 00:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b7a4736-c54f-3116-b20c-83f23630f30e | -1.7292 | -47.16 | 2026-10-10 00:09:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a569e4e-bf9e-3b5d-bc49-e6cad4ebb447 | -10.044 | -44.352299 | 2026-10-10 00:09:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ce68b56f-de4d-30a4-8ac8-712a4b155b5c | -13.9355 | -42.9734 | 2026-10-10 00:09:00 | METOP-C | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 350626bf-76a2-3302-a132-f7a24d58582b | -4.3925 | -43.1264 | 2026-10-10 00:09:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6b03467-1ef7-3746-be3c-98099b637131 | -11.9999 | -43.447201 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34a0e142-d11b-34fc-81ea-0a8155d961ab | -5.5491 | -43.966801 | 2026-10-10 00:09:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85c17f73-7a68-36da-a0d4-f21009081e0c | -7.2243 | -40.355202 | 2026-10-10 00:09:00 | METOP-C | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 30475b0a-6be8-32ba-87cb-5d5fec76cafc | -18.3288 | -42.392502 | 2026-10-10 00:09:00 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a22e5458-47c4-3c23-9c7c-6db5293779b8 | -14.4477 | -43.922401 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 41b67945-c6d5-36a8-891d-2f3cec4f99d8 | -10.8816 | -44.8311 | 2026-10-10 00:09:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a5c089a-fe30-34f5-bdb0-384f4eb24ae2 | -9.8294 | -44.783901 | 2026-10-10 00:09:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7e66f8a4-f3ff-3bd2-a50f-16de7bf4d1f6 | -13.2511 | -44.005299 | 2026-10-10 00:09:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02bcfd27-4a46-316d-977f-ac645e330873 | -9.2895 | -47.3992 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46bbf70c-e44c-3b11-84e0-42ecee13425a | -16.649799 | -40.543999 | 2026-10-10 00:09:00 | METOP-C | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fed30c51-00db-31e1-bca8-d849c08e64a0 | -9.6169 | -48.891201 | 2026-10-10 00:09:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4ca83d0-8aa9-37b9-9a70-d4b9abba068f | -8.1892 | -45.763901 | 2026-10-10 00:09:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00ab0a5c-dc5d-385d-844c-6698485c4b93 | -3.7914 | -45.794601 | 2026-10-10 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 643a9a27-cd80-36bf-a761-e56edbdc1a20 | -4.9023 | -43.468899 | 2026-10-10 00:09:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aad916f8-5cb5-38f7-93e6-b405ab2803bd | -9.0035 | -44.369301 | 2026-10-10 00:09:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6cb02f15-d699-3c65-83f9-20b80c716ba6 | -13.3652 | -43.915298 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 94e9c760-5df5-3a00-8faf-ccda2eae3fec | -4.3604 | -44.3503 | 2026-10-10 00:09:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0cd1ef0-f623-3b43-8311-735f6d3b4936 | -15.3716 | -41.915501 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3214fa41-3d6c-3cf0-b17d-2f63249a4107 | -4.4153 | -47.534302 | 2026-10-10 00:09:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62895665-9771-3ab9-a1b8-a5293fad7c83 | -5.9453 | -40.938999 | 2026-10-10 00:09:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7e754b2c-06f5-3eb0-934e-7f6226662915 | -5.745 | -45.122601 | 2026-10-10 00:09:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 640fb891-9417-3260-87aa-d2f394a46658 | -11.9881 | -43.439899 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dc731529-f4ba-3484-967b-9638b07062f8 | -5.2191 | -50.694199 | 2026-10-10 00:09:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81e1f0e4-4e11-30ae-ae3b-378d9dca6c71 | -9.6129 | -48.871498 | 2026-10-10 00:09:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df0fe41b-802f-36d9-b063-d2c496479453 | -7.0623 | -40.9552 | 2026-10-10 00:09:00 | METOP-C | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 445478a3-4ef5-3a54-aadc-6b8ff5b3e1fa | -16.1828 | -39.333199 | 2026-10-10 00:09:00 | METOP-C | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb3c0457-4acb-3e71-8ae5-a330bfbceb04 | -4.4478 | -47.9118 | 2026-10-10 00:09:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 855a0113-8b74-3c98-b9a0-6f81fdbb58d6 | -12.2111 | -44.846001 | 2026-10-10 00:09:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5ef7925-33cf-3524-aaaa-d766494e7c5a | -13.376 | -43.869301 | 2026-10-10 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 014a3028-65c3-3f96-affe-50559dffce66 | -8.952 | -47.389099 | 2026-10-10 00:09:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72c8d218-0e03-3c2e-941c-b0b2c1800781 | -7.0642 | -41.599098 | 2026-10-10 00:09:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ec42660f-7d1b-3af4-9f03-0f1539f3c6e4 | -14.4589 | -43.9772 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d94829ec-b90a-332c-9a1f-7b385bfb43c3 | -7.7703 | -43.793301 | 2026-10-10 00:09:00 | METOP-C | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 168aa683-85ac-3b78-b5c0-3c269eefd61d | -14.0175 | -48.780102 | 2026-10-10 00:09:00 | METOP-C | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 981ea63c-17ad-3b32-b2d6-a045ca7eb319 | -4.5064 | -43.6297 | 2026-10-10 00:09:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a1bebae-61d2-35d0-bc2a-91907560dbb6 | -4.3146 | -41.247299 | 2026-10-10 00:09:00 | METOP-C | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f9fa2196-9d2f-3f43-94de-b011b4dde51f | -9.2766 | -47.385799 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 835dce98-5d85-3174-8b66-1f998c22d64b | -14.8043 | -42.334301 | 2026-10-10 00:09:00 | METOP-C | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e5d40546-6604-3140-b6a5-67da06d3eb7d | -5.528 | -43.049099 | 2026-10-10 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b17c7c15-b91c-31b7-a398-b9ec99c2f01e | -17.9515 | -42.4939 | 2026-10-10 00:09:00 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b24fdc9c-88e2-334e-b884-c1e9bd53427e | -15.3814 | -41.913399 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README8.md)
