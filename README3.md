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
| b06e8c19-1d70-3e83-ac1a-056536c72854 | -12.65981 | -48.23267 | 2026-07-15 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13eb1372-978c-36be-9a55-176cf2e05eea | -17.34517 | -42.6292 | 2026-07-15 03:55:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f39d0ecf-8b36-3703-89e9-43e9feb96dd3 | -13.535 | -47.77862 | 2026-07-15 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 942aea3f-1103-3a3b-b214-e3f85ca1a2d0 | -20.34952 | -40.32792 | 2026-07-15 03:55:00 | NOAA-20 | VILA VELHA | ESPÍRITO SANTO | Brasil | 3205200 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6823a734-9462-3ce7-b928-d8461f8c38aa | -15.67662 | -40.85955 | 2026-07-15 03:55:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4f2fae6b-e2af-3ab9-bea7-c241bc23369b | -20.16207 | -41.66111 | 2026-07-15 03:55:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b1b6a483-b390-3e1e-86dc-04f8a4b5918e | -17.52439 | -44.11523 | 2026-07-15 03:55:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e6ddcbb-0809-3edc-b3e5-d015869ddc40 | -12.35822 | -47.41858 | 2026-07-15 03:55:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ea40d20-fe77-31d6-a9f7-888ba93cfe08 | -15.77945 | -47.79676 | 2026-07-15 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47461c55-d7ef-37b0-89be-27b9f109796b | -17.34084 | -42.63283 | 2026-07-15 03:55:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3af64d25-b1de-3611-b561-35a46e0ab745 | -18.49021 | -46.95185 | 2026-07-15 03:55:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0f6b3d43-f312-365a-a8d2-0a1012766289 | -13.44443 | -43.84692 | 2026-07-15 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 67f96c4b-c35e-3307-bab9-96054ffa7ed9 | -18.78596 | -49.08452 | 2026-07-15 03:55:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6dd3e96-fbc4-3f80-a21b-8a79a50d85e8 | -17.33368 | -42.63146 | 2026-07-15 03:55:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db7ac81f-b862-3633-ab81-de04060a9051 | -18.14725 | -46.91338 | 2026-07-15 03:55:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90d19f57-5819-308c-9471-bb5c26635575 | -15.9373 | -48.06693 | 2026-07-15 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3539d6e-e7f6-3fc8-afa5-66ddd0eed2aa | -12.3595 | -47.41205 | 2026-07-15 03:55:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e7fa2dd-a10f-3d08-9f28-b06f09da9eea | -15.77882 | -47.79991 | 2026-07-15 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bad15bdf-fef1-3351-ba6c-69718769a4bf | -17.52586 | -44.11268 | 2026-07-15 03:55:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92beb4ee-a52b-38b3-870e-a7b5c1f44492 | -12.35886 | -47.41533 | 2026-07-15 03:55:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79bd8cc1-f384-3bd3-aa14-79a2871d1667 | -17.33726 | -42.63214 | 2026-07-15 03:55:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 763e3d45-c48a-36bf-b73e-78249cfad045 | -18.49481 | -46.95248 | 2026-07-15 03:55:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8fb05945-054a-3488-92c3-b0b14beb848a | -13.43968 | -43.84996 | 2026-07-15 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6796f18f-4ece-30cf-be39-a7c8af2e4d3f | -20.69186 | -40.52388 | 2026-07-15 03:55:00 | NOAA-20 | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| de72d640-6f1c-353e-af1d-c993a3962e74 | -13.43634 | -43.84656 | 2026-07-15 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8657330d-dc1a-3d86-9929-5875b0307fb0 | -13.53438 | -47.78177 | 2026-07-15 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5d3ff67-19ee-39f9-a47c-4c78890d95b1 | -13.53561 | -47.7755 | 2026-07-15 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db4f1a73-dc98-3681-8c4c-c7c8db635810 | -19.96233 | -47.20472 | 2026-07-15 03:55:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17b7b996-ae87-3b2b-89dd-0892e6ccecc5 | -18.78039 | -52.40837 | 2026-07-15 03:55:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1466d502-4944-3c46-8751-238f522d3e55 | -13.27175 | -45.1751 | 2026-07-15 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecb27403-c09f-341e-80de-5221fda113dc | -18.78088 | -49.08296 | 2026-07-15 03:55:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3f084a6-ee18-3d0f-8418-d56ece5e6760 | -18.48759 | -46.9411 | 2026-07-15 03:55:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93cc30d8-ebae-381a-be27-6502a36d3ca2 | -18.49583 | -46.94723 | 2026-07-15 03:55:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b65d3a32-6699-38e9-9532-33041534a841 | -14.30347 | -47.173 | 2026-07-15 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c7bd838-7262-3a17-bf97-14d18c06750a | -20.34894 | -40.33159 | 2026-07-15 03:55:00 | NOAA-20 | VILA VELHA | ESPÍRITO SANTO | Brasil | 3205200 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e9f90d95-4dfd-38f7-a517-8c434fe1dbd7 | -13.43628 | -43.84555 | 2026-07-15 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 935302d4-bb59-3192-9f99-202b8f235fca | -17.34442 | -42.63352 | 2026-07-15 03:55:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e661611c-ff6b-3c39-a482-13f5bbd35abe | -15.93665 | -48.07013 | 2026-07-15 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f57c2c8-3ca5-3002-961c-afb6941d4a23 | -20.78077 | -42.75594 | 2026-07-15 03:55:00 | NOAA-20 | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d43aa12d-fbdb-3c06-aa4c-f1031d94a4f0 | -13.27259 | -45.17053 | 2026-07-15 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fff94d3e-2e8e-3df1-80a0-38f5ebe735d2 | -20.64945 | -43.4253 | 2026-07-15 03:55:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 82ef07b7-38d4-37fe-8ade-4416403670a0 | -13.26898 | -45.16516 | 2026-07-15 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 334d6e05-8f62-38e7-b109-45dce66cf3d2 | -20.0883 | -42.51365 | 2026-07-15 03:55:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a920bcae-80aa-385d-92f8-ed7ddfa818a7 | -14.80367 | -41.67395 | 2026-07-15 03:55:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 116d21a2-08a6-39a3-b8a2-956e2b32c29e | -13.41874 | -44.17449 | 2026-07-15 03:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 726e6ae7-f63e-3f04-88cb-0e17e27f1df8 | -13.2762 | -45.1759 | 2026-07-15 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c05e85a2-33ec-3caa-9017-b2270fb1fb56 | -17.52199 | -44.11196 | 2026-07-15 03:55:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5663af8-1c0f-3fac-b30b-1400d66a8779 | -13.44036 | -43.84624 | 2026-07-15 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 26ab945e-6859-32c5-b190-298ee6f83529 | -18.49219 | -46.9417 | 2026-07-15 03:55:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bdb9026e-f88c-35d6-ae33-2cb838495082 | -22.37731 | -49.79251 | 2026-07-15 03:57:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dd794103-d93d-367a-98ab-a6019f10e913 | -23.56141 | -47.51284 | 2026-07-15 03:57:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.9 |
| 13e3d4ec-bdd4-365b-bce0-d1fba2de462b | -20.22413 | -50.91796 | 2026-07-15 03:57:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 23e1e228-593d-3556-b8c4-821577c8eaf4 | -23.79625 | -48.451 | 2026-07-15 03:57:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 318c7105-3a62-34b9-92c6-5b0ad1f3cd40 | -21.47744 | -47.34003 | 2026-07-15 03:57:00 | NOAA-20 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1de1cf28-adc9-3d7a-8bc9-93a52726e4e8 | -21.53587 | -41.21231 | 2026-07-15 03:57:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 74cc2b20-f404-37c7-99c7-f728ba71c2a9 | -22.96153 | -52.70557 | 2026-07-15 03:57:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a711fbd4-33b4-3335-944b-5d55d0f42d8c | -22.6883 | -49.21589 | 2026-07-15 03:57:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c29c016c-4929-330c-a2ff-51d0bb2fe8e3 | -20.72091 | -43.42962 | 2026-07-15 03:57:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cf487e16-671a-3706-b9ae-a05b9783a6f7 | -22.70067 | -43.36057 | 2026-07-15 03:57:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| aafa263f-06a2-3194-b21c-3c08d9c609dc | -23.55432 | -47.43835 | 2026-07-15 03:57:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 69952c2d-9da0-3d3d-a05e-291308509c1d | -21.4783 | -47.33572 | 2026-07-15 03:57:00 | NOAA-20 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2885723e-23ae-3f5b-8a14-91160dcf9dbf | -23.79177 | -48.44989 | 2026-07-15 03:57:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b6951800-b8a2-3216-8a54-74f7677c8f7a | -23.01904 | -46.67505 | 2026-07-15 03:57:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5d677a7b-8de7-3022-a926-cca07b40928c | -20.22505 | -50.91388 | 2026-07-15 03:57:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9a541022-39c3-3bc2-9845-285edbf1eeb4 | -22.96378 | -52.70963 | 2026-07-15 03:57:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 471af926-1d63-3083-84b5-96cfdbb415dc | -22.10006 | -46.99604 | 2026-07-15 03:57:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13626cb2-e406-333b-ab4b-5a7040415cc8 | -20.30176 | -46.35847 | 2026-07-15 03:57:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4d6beba-3b8c-3cb0-9d07-5582b78f0a58 | -21.47303 | -47.33918 | 2026-07-15 03:57:00 | NOAA-20 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 93d0d0c5-1c92-3786-9102-2705b258a58f | -20.65173 | -48.6783 | 2026-07-15 03:57:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9af4bd60-2d33-3daf-84f6-8626cd00af03 | -21.53254 | -41.2117 | 2026-07-15 03:57:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8570ed54-8662-337f-a763-fd1f9ff1da7c | -23.13675 | -48.66882 | 2026-07-15 03:57:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ebc4aa5-8387-3bd2-b0cb-52adca5f57a0 | -23.55222 | -47.43528 | 2026-07-15 03:57:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2154befd-6028-3bc5-85cd-81bc893a1ed4 | -22.96485 | -52.70516 | 2026-07-15 03:57:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ff36c63f-0e7e-378a-bdaf-77d4fc54fe76 | -5.35378 | -45.18283 | 2026-07-15 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c10f2702-d0e7-3564-8603-9c3ac682c0ad | -2.7238 | -49.78905 | 2026-07-15 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eeeab875-f7b7-3543-a2c0-05fb4553a22b | -3.15745 | -48.58113 | 2026-07-15 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8dbfcbc-787b-32fd-9313-c869d028ac7d | -3.68637 | -49.42149 | 2026-07-15 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81a2c900-36f3-3d60-97df-e77df389bb9d | -5.82822 | -43.59229 | 2026-07-15 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b520786-c288-30e6-96a3-9e269a1d6b38 | -3.15469 | -48.57719 | 2026-07-15 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 536ed42d-4906-3bda-9eee-bb30b2b4559a | -5.0147 | -37.5431 | 2026-07-15 04:38:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2e5fa863-cfc1-3c47-8c6e-b8135267517f | -5.01305 | -37.54306 | 2026-07-15 04:38:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6fb8a0d8-ff0a-3b0b-9e50-7e5629e2e8bb | -3.15415 | -48.58062 | 2026-07-15 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57a1446b-de64-37a1-906a-7e46745a88cd | -5.39772 | -45.147 | 2026-07-15 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af1d781d-c9a7-3249-945e-803dcf9d7df0 | -3.14348 | -48.14981 | 2026-07-15 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93269811-5b7b-37d1-bff6-dd1b0c3ad3b5 | -5.35001 | -45.18227 | 2026-07-15 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4230a21-b101-319c-b31b-34526b906c01 | -5.82878 | -43.5885 | 2026-07-15 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3404018e-39cf-3153-993f-9e98e2b2d067 | -3.22081 | -49.48345 | 2026-07-15 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f016c859-61f3-331a-8efc-e98bd757e551 | -5.34624 | -45.18171 | 2026-07-15 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4bb3e6c-4df6-33d1-898d-cd294441261a | -1.65916 | -54.4591 | 2026-07-15 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b697818a-8a16-3838-969f-1b75b7b6d988 | -4.086 | -47.3128 | 2026-07-15 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e941f87-7c7f-35b7-a511-9c6b13332e4f | -3.85937 | -54.08131 | 2026-07-15 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b71a4048-a05a-3df9-ad39-107fbeca6386 | -2.76794 | -48.57287 | 2026-07-15 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b8268f9-cc3c-3ab8-ab51-6b01de54c6a0 | -1.6635 | -54.45971 | 2026-07-15 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e98fddd-d2d9-35bb-97f6-797ce5fb76ed | -5.01862 | -37.54898 | 2026-07-15 04:38:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| edbbdedf-1ae7-3217-af99-fa87ef948dcb | -5.014 | -37.54799 | 2026-07-15 04:38:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3e04f39b-fafe-30b5-9fc5-657c4746ed26 | -1.33589 | -48.32688 | 2026-07-15 04:38:00 | NOAA-21 | MARITUBA | PARÁ | Brasil | 1504422 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0749728-23aa-3486-a577-d96eb3356990 | -3.14678 | -48.15032 | 2026-07-15 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a87e768-b35e-3a3d-a705-314eaa3e463c | -0.16526 | -50.40647 | 2026-07-15 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ba167c7-0f07-3bfb-bd0f-c424f6296521 | -5.12316 | -43.23816 | 2026-07-15 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 053728de-52cd-3f4b-8413-7da282913e78 | -5.34934 | -45.18687 | 2026-07-15 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README4.md)
