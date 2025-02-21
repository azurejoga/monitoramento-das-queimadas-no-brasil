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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42e5f064-ea1d-34ad-b5d9-a03af4a96930 | -6.4671 | -34.9813 | 2025-02-21 04:00:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 195.0 |
| edc958f4-8edd-3663-b002-9461fccdc78d | -6.49 | -35.0 | 2025-02-21 04:00:00 | MSG-03 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f98a528a-d02f-3289-8140-e3157f20c137 | -6.09581 | -37.43409 | 2025-02-21 04:08:00 | NPP-375D | MESSIAS TARGINO | RIO GRANDE DO NORTE | Brasil | 2407609 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0817361e-1e26-39c1-b96b-186807b0415c | -6.46456 | -36.66071 | 2025-02-21 04:08:00 | NPP-375D | ACARI | RIO GRANDE DO NORTE | Brasil | 2400109 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 90875d9e-80f0-3016-af46-8d84563d5c8b | -7.41886 | -35.12734 | 2025-02-21 04:08:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 023692fc-4ae4-3e60-a34e-67f816e0ce4f | -6.47243 | -34.99593 | 2025-02-21 04:08:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| 9347591d-1ceb-3374-b0f3-38a2321d56ca | -6.47824 | -34.98747 | 2025-02-21 04:08:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 38.8 |
| 1901bcbd-34f6-3fad-97e8-d198baa0d996 | -9.93077 | -37.23844 | 2025-02-21 04:08:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6ec3b539-2286-3bab-9334-395a45cd2549 | -6.48147 | -34.99719 | 2025-02-21 04:08:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 71292fba-b0b5-3ffc-8dba-d650bd0ce2dd | -6.97608 | -43.00775 | 2025-02-21 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cc17ebc7-733f-3b0d-9788-fc1deb48b15e | -5.67489 | -45.23166 | 2025-02-21 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89118b37-f5e2-3c85-baf8-4f4573c588e1 | -7.4234 | -35.12794 | 2025-02-21 04:08:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4a9079b8-4e51-3ac0-8a71-dd97065e46d2 | -6.47759 | -34.99201 | 2025-02-21 04:08:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 38.8 |
| 90bbaee8-7a39-3c3c-a583-b921cd285a97 | -6.4834 | -34.98364 | 2025-02-21 04:08:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4f508797-3f9e-3bd9-ae75-73e1c02bfa9e | -6.48211 | -34.99269 | 2025-02-21 04:08:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2c2e7b55-2318-3949-ad4c-a536153f9055 | -6.21039 | -48.06316 | 2025-02-21 04:08:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dff71df7-8e1a-38a9-8182-6a746f53794f | -6.47695 | -34.99656 | 2025-02-21 04:08:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| 22dbe298-0a43-30e3-949b-3072759b5887 | -5.87945 | -48.10849 | 2025-02-21 04:08:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fe7b3d0-53e5-314b-86eb-f9b2720c1887 | -6.48275 | -34.98815 | 2025-02-21 04:08:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ad205248-439d-3a68-9489-72934575ea56 | -6.48727 | -34.98882 | 2025-02-21 04:08:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f6e66031-965a-338b-98ca-b9a5a73e6b6e | -6.97492 | -43.01493 | 2025-02-21 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dc11d573-c0b0-389a-a0b2-349f6ad0894a | -6.47372 | -34.98685 | 2025-02-21 04:08:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 38.8 |
| 588111e2-9b5c-3bee-900a-96dd29dd990d | -6.9755 | -43.01134 | 2025-02-21 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4bab99bf-1cbc-3d48-8b9d-72fd87a37e05 | -5.47655 | -46.16104 | 2025-02-21 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 262791b3-22ac-3526-b49e-0f18ec488a96 | -6.47631 | -35.00105 | 2025-02-21 04:08:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| 26e24881-67f3-3260-b257-597837618c91 | -6.97944 | -43.00829 | 2025-02-21 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8f48371b-1b79-3923-88ac-8533c0c9e091 | -6.97434 | -43.01852 | 2025-02-21 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f3584ce7-4653-3de4-9701-32f071ac0099 | -6.97886 | -43.01189 | 2025-02-21 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7f3f2cf1-1467-301c-afd6-a982954be27b | -6.47179 | -35.00044 | 2025-02-21 04:08:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| d80dbf02-987d-31be-88b5-9b35d9980b18 | -12.56143 | -44.74347 | 2025-02-21 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40975233-1e6d-348a-a53a-8040aa709d4a | -17.67451 | -42.74254 | 2025-02-21 04:10:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ff218d1-56b6-3c80-8bca-a6af1f950317 | -14.45293 | -47.90921 | 2025-02-21 04:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b40b604-e390-3b61-b4b2-db6bcce77508 | -12.80504 | -45.0087 | 2025-02-21 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b806da3e-2046-332a-9a76-f0bc1ab547e5 | -16.78329 | -49.619 | 2025-02-21 04:10:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8badf563-44d4-3b48-b731-1eefd1e5fbca | -14.11041 | -45.66587 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dd7eb2e-ee21-337f-ab0c-e780721bd550 | -14.83686 | -45.19514 | 2025-02-21 04:10:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c292931a-c0e3-35a4-bb8f-3a40bf407917 | -17.46134 | -47.01115 | 2025-02-21 04:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e11b3530-5135-31c1-a5bc-261652dc4964 | -17.46475 | -47.0276 | 2025-02-21 04:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12443ec1-f370-3d2c-b128-4fca186425cd | -12.7988 | -45.00371 | 2025-02-21 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcd0d0ae-3514-30dc-87c7-798723ec04bf | -14.4389 | -45.63732 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9366b19-f245-3d79-8ae9-d711d58ac3c7 | -14.11322 | -45.67036 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8dc2e05-7dca-3ed6-8110-f0440d52c83f | -14.43609 | -45.63282 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 305b2a9d-e600-3768-bb80-09a098365b63 | -13.53208 | -46.50792 | 2025-02-21 04:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b33d8e8b-75e4-3084-ad34-e0c9108b99a1 | -14.42572 | -45.631 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d8b0bed-f699-3a9d-adc3-6e58dd2156ea | -16.78504 | -49.61956 | 2025-02-21 04:10:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4bde953-e6f3-368f-bda3-2a68f4797d03 | -14.45424 | -45.66322 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30d0f3d4-9fd0-3eb6-b240-e6f9c150258c | -14.43826 | -45.64121 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccc3f31a-c992-3195-b803-bb12759acf6f | -12.56484 | -44.74405 | 2025-02-21 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79d184d3-e9b9-3439-9ced-2cf05099f368 | -12.45357 | -43.62309 | 2025-02-21 04:10:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8f41c0a-49ca-3da4-8635-75fee74f8767 | -15.75146 | -42.96917 | 2025-02-21 04:10:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 935cc272-75cf-3395-b523-26807c9899f1 | -17.46205 | -47.00698 | 2025-02-21 04:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66c3046d-2b4b-3d54-b15e-44e15463a4c5 | -13.53237 | -46.50595 | 2025-02-21 04:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89dc23f7-95da-3187-9379-07f6450a3132 | -14.43957 | -45.64465 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccfde4d3-330c-3440-8313-f02c781b593b | -17.08341 | -49.3881 | 2025-02-21 04:10:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d2b9995-0399-3ca7-9732-fe3b398a081b | -11.10824 | -45.11929 | 2025-02-21 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2d62676-bf31-35ee-a650-59cdefa6fa2d | -12.32093 | -46.66748 | 2025-02-21 04:10:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae5f7c9a-8fae-3d64-a639-5a87b8ee2351 | -12.80223 | -45.0043 | 2025-02-21 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68aa3a96-b9df-3a61-8e4d-ae16e56c0086 | -13.75411 | -43.48356 | 2025-02-21 04:10:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49f291d7-bcce-379a-be67-b4d123c58433 | -17.4578 | -47.01049 | 2025-02-21 04:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 415b6a77-7360-34dd-b189-7320de91d48c | -11.57724 | -47.63555 | 2025-02-21 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11d8a170-d0dc-34ab-b985-39add4c86da7 | -14.4577 | -45.66383 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efc894b3-258e-3b38-a339-00d59d47cdd8 | -14.43199 | -45.6361 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cd7e8eb-f369-3e0a-b9a0-6d782cdda4bd | -14.42982 | -45.62772 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a99c109a-17de-3d94-ae1d-7cb0e35224d6 | -11.57327 | -47.63482 | 2025-02-21 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc0267fd-3efe-3576-b2f7-5db4a56a2755 | -14.44236 | -45.63793 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5f8c01f-ffa9-30cb-a9d3-7c02d7ea0de2 | -15.73089 | -43.14736 | 2025-02-21 04:10:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fa7be259-eae4-325f-a8b1-787b0fe59e28 | -14.68151 | -43.04765 | 2025-02-21 04:10:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c89edf96-2a26-3f16-89e9-058ec1ab77c9 | -15.39189 | -43.73989 | 2025-02-21 04:10:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d25e604c-33ab-371b-ade3-7e5c669c9483 | -13.96006 | -48.50685 | 2025-02-21 04:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b5f29ed-e3b3-3cc6-afa6-c6417a1016c7 | -11.85347 | -46.94142 | 2025-02-21 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95dbfc45-7d7c-3ef1-861f-00c5b0d37b46 | -12.35501 | -47.9919 | 2025-02-21 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f9c8336-1753-3e45-a9b2-d16f47f0684f | -11.86486 | -46.94335 | 2025-02-21 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6e4971b-165c-383d-ab53-81af31da0eba | -14.43416 | -45.64449 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af0c6a24-23b3-34c0-9e67-eeeac1a260e6 | -14.43327 | -45.62833 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed922eab-3d93-3414-90e1-0b94655cbfd4 | -14.44089 | -45.63689 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa617b26-a1b1-3c94-b5ca-d907ba1e50f6 | -17.86957 | -45.54683 | 2025-02-21 04:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9d63d75-8305-3f5c-a9de-f1e938150cab | -11.80304 | -46.65322 | 2025-02-21 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3b37881-ced2-3e5a-acb1-6d488e42c04d | -12.80442 | -45.01249 | 2025-02-21 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9233b3d-1246-3eed-b9b5-8de4dbe8cda0 | -17.05082 | -45.0405 | 2025-02-21 04:10:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4d70d40-d7b8-3524-b925-352708448d7a | -14.4348 | -45.6406 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63f0a94c-3149-3421-9820-dfc420f41926 | -15.57032 | -47.85455 | 2025-02-21 04:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5019f219-7df8-306a-b8ed-8f2133c94736 | -16.68124 | -43.88354 | 2025-02-21 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df58d4da-c04c-3e8f-a528-e7bf4abe27ae | -14.11289 | -45.66662 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be34f9a7-d1ae-344f-89c3-65385fd6677e | -14.44023 | -45.64077 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57026900-ac36-3e9f-a799-7751ed687a7a | -16.73621 | -48.1156 | 2025-02-21 04:10:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d923726-b007-350a-be60-00b95014fcc4 | -12.16137 | -44.18366 | 2025-02-21 04:10:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8c9348a-9b15-3e0a-8952-ad0fc2a8adfe | -14.43892 | -45.64853 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b42940dc-d5de-3639-9cd1-6833b284d9bb | -12.17371 | -37.95542 | 2025-02-21 04:10:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f6341937-0250-3790-8998-3709b5ffa541 | -15.55797 | -46.27441 | 2025-02-21 04:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ea85025-9379-3acd-b105-b8cb688ccc9b | -12.35099 | -47.99119 | 2025-02-21 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d359e84-a20d-33e7-96f9-b36633f39c0f | -11.80677 | -46.65391 | 2025-02-21 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7707ef5-0f97-33c2-bbd9-e96658d20ef9 | -11.85727 | -46.94207 | 2025-02-21 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97c60b77-025a-3a68-9b56-dae61ad1836b | -17.37913 | -42.48289 | 2025-02-21 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 168cab21-3d6e-382b-a4f8-025a08d4ef93 | -13.68132 | -42.36518 | 2025-02-21 04:10:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 766978e2-6d50-37e0-96a6-65c8482df600 | -14.11225 | -45.67051 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47f1f19c-efb2-31a0-b1d5-e9e2192429b7 | -13.53281 | -46.50356 | 2025-02-21 04:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fdef72e-73fc-395b-9b99-0be883809d27 | -14.43263 | -45.63222 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df0cb191-a088-3b6d-95b9-631b017d59be | -17.46348 | -47.02014 | 2025-02-21 04:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bba0488-9543-3894-a0a5-594d6535d2c6 | -14.42507 | -45.63489 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45e09c2d-43da-34f5-9bb2-631e3a6c28e8 | -14.43698 | -45.64899 | 2025-02-21 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README4.md)
