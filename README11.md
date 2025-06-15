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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0079fb3e-2111-382a-9504-112b37919ad3 | -15.40331 | -47.85632 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bfdbfd7-7b89-357a-a9aa-678a1076e774 | -12.69419 | -52.39692 | 2025-06-15 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d2b3d412-4262-3b8e-bea0-d8e74b94800e | -13.9228 | -54.61694 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 00d6a511-261f-3d40-ba69-4dc5f353b23f | -17.75995 | -52.43226 | 2025-06-15 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1039eed4-2337-351b-b309-1f6def00360a | -16.35014 | -43.6978 | 2025-06-15 04:49:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7bb98d8-21df-3dda-8951-0edabd99ca7a | -15.40455 | -47.87898 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca1893e3-eb33-3a89-ab4f-8ede7a547b5c | -13.94672 | -54.44885 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 601c564d-9eb1-31d8-af1e-97f66c6c1e73 | -15.40141 | -47.87119 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f15f020f-f99b-37ee-b10e-14fc47b122c5 | -13.92063 | -54.6089 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 23e57018-e3a4-3925-8e4e-05ea97469a7e | -13.91262 | -54.61526 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 4e8f66ec-f4b5-3d45-a10d-bbf770003671 | -15.40003 | -47.88188 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1a2a29e-d108-39c8-b7e3-5ce318279a2a | -14.67155 | -53.13029 | 2025-06-15 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50475c8b-70f4-3a8f-9591-1219abecd467 | -13.92496 | -54.62503 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 4280fb4a-6920-3034-9dbd-4ae5f2b9e47b | -16.28705 | -52.93277 | 2025-06-15 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 651ed318-2177-3872-a4da-45e739a0f12f | -13.23163 | -49.83725 | 2025-06-15 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fd72774-43d5-3700-a2e3-49ab732ded13 | -15.40862 | -47.87952 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba2793fd-68b6-3208-9527-1403e7ad3a67 | -13.90584 | -54.61415 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d5e66b0d-c84b-3a66-b2f5-6d737f4bf5fe | -13.22868 | -49.8326 | 2025-06-15 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 455a90d0-2834-36cb-8300-af9a7c98c37d | -13.90767 | -54.60295 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a08ed15b-0ff9-39e0-a765-569a675ee79a | -13.91757 | -54.62764 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ad29940-3d22-3994-9818-c26378de4b7d | -15.41003 | -47.86855 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdd7ffc3-549d-3c17-b562-6e5102a861a8 | -14.83206 | -48.43552 | 2025-06-15 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 61980eca-d92b-34bc-a158-922679d62d45 | -13.9188 | -54.62012 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| f50c7bc2-a463-3e3b-87de-b9fa169e927f | -18.39264 | -44.19028 | 2025-06-15 04:49:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1db3a67-0f1f-3f57-a753-b11877693f8d | -13.91329 | -54.65383 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66e53c96-1494-32d4-86cb-7a68b21db924 | -15.40956 | -47.87223 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc7c078d-e150-330f-938c-009e203a28b9 | -16.2898 | -52.93691 | 2025-06-15 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c626aca2-27c0-37a4-b3b7-a759a9ab10d6 | -13.95009 | -54.44944 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94e55ebd-2fa8-39d3-ae2a-8f6b7cc7d581 | -13.77672 | -54.30249 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fe0c335-dafe-31ef-b53a-6227f6d0def0 | -13.92158 | -54.62444 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| b2be5912-70bc-3842-b5c6-e4936bb392b7 | -15.41099 | -47.86109 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 061825e6-7a7c-3a7b-a66f-29bf4749b50d | -14.67099 | -53.13384 | 2025-06-15 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68ad0e3b-637e-3ab6-91df-982923aebdc6 | -18.39598 | -44.1904 | 2025-06-15 04:49:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| daa4f410-113c-3873-a959-73131431ef60 | -13.91107 | -54.6035 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f5672fa2-b718-3a45-a21d-efc128e07781 | -13.91851 | -54.64319 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 373a2c53-edde-30f9-b806-c0ff1f90f826 | -16.29036 | -52.93332 | 2025-06-15 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67e19f7f-5e5a-3694-9697-277fbddd6682 | -13.9139 | -54.65009 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9d18dc5-e3fe-3a30-a3f1-e938c827f94d | -13.91785 | -54.60463 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 62193370-b5d6-352b-b0cf-2582d7da3030 | -13.95526 | -54.43893 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e16178d-b537-3dfc-8b86-a7acdc9989eb | -12.26631 | -54.53436 | 2025-06-15 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd3f7dbd-c19f-3470-9ace-309294ff726d | -13.92124 | -54.60519 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ccd3e845-1d36-34b8-a805-bceb52a71043 | -12.35823 | -57.43103 | 2025-06-15 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d97f1fe-70f7-35e8-b809-540db8ddd80a | -14.03818 | -55.13379 | 2025-06-15 04:49:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d92779d-7ee0-3814-90d0-59e28c2787c2 | -13.94743 | -54.48711 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de832dac-9f7c-3a10-abc7-6e20caae4e23 | -13.91602 | -54.61581 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 736d33d0-d862-3da5-bead-c9bc8faca7a3 | -13.91324 | -54.61151 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 1955212b-fcd1-39cd-904e-ffa9183c5cd9 | -14.83273 | -48.43056 | 2025-06-15 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4a0d6c1e-c28c-3c4c-8653-d58de2c7104d | -13.89967 | -54.60926 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c07e9f9-0026-3146-8a1d-ecb174cf340d | -15.40408 | -47.88253 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c88db146-e836-31eb-b132-103fd58b14be | -13.98365 | -56.02033 | 2025-06-15 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98cee00d-a0ba-3efa-8b47-9ebf59513c2c | -13.91724 | -54.60834 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ac14223e-5109-386e-b44f-3970c1b224bf | -13.92096 | -54.6282 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 17c06b20-f16f-31fd-ba5a-7c09d4f2cf16 | -15.18501 | -50.84919 | 2025-06-15 04:49:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccf89d51-1213-3ea9-851a-abb701a355fa | -12.68759 | -52.39585 | 2025-06-15 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 225ff4ba-fe15-3e2f-8a67-b39df4d49988 | -15.40741 | -47.85674 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0d25796-9612-3aac-b8ff-ab83303b54dd | -14.83922 | -48.44129 | 2025-06-15 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e63ef34b-afe7-399e-a122-296a8bf89d3f | -12.16873 | -56.54227 | 2025-06-15 04:49:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51353dbf-10df-39aa-a6ce-721d3c3d2e2a | -13.95803 | -54.4432 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a5a7483-7d1a-35b1-8166-ec2afdf69a89 | -13.90923 | -54.6147 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 69a75fb0-4b3a-335c-b5a3-fbda9ac98abb | -13.91201 | -54.61903 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55fc662d-ae23-3ccd-bb46-c5df6df78614 | -13.90862 | -54.61845 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f80da055-eff8-370e-86c9-437cb55641fe | -14.67429 | -53.13438 | 2025-06-15 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21d6bfab-e98f-36ef-8b64-bfc618a01208 | -13.91451 | -54.64634 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72b1169f-6d6d-365c-b25c-0d5aa348249f | -13.91941 | -54.61637 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 3ac97450-28e6-3aa2-a5c6-43236ea6069e | -12.69364 | -52.40043 | 2025-06-15 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| daf80b10-893b-3d10-a644-f44330f1c6a7 | -13.91845 | -54.60092 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 298950c7-5fbc-3b38-8076-857f91ca068f | -14.03193 | -55.12872 | 2025-06-15 04:49:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2933c6f-ab4b-3e89-b854-808967465a32 | -13.28866 | -57.06965 | 2025-06-15 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71991b97-ba9f-3139-ad6a-7adec0041e08 | -15.6426 | -49.37425 | 2025-06-15 04:49:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e73f06ba-c973-3a76-a405-d0011fa95fea | -15.40227 | -47.89659 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29fdfce5-6e3d-375b-8048-b30c278dfce8 | -13.91045 | -54.60723 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e305cfb6-5dae-31df-bcff-6936fc791961 | -13.91479 | -54.62333 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 59becc63-a8b2-38fc-a406-f31dff156aca | -13.9059 | -54.6291 | 2025-06-15 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| b4a44c8b-77ab-39dc-acd6-a26ff3f1acb7 | -13.9062 | -54.6084 | 2025-06-15 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 137.0 |
| fc7839d2-1224-34d4-8226-ccf1bb9d2a8c | -13.9065 | -54.5878 | 2025-06-15 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 4c8c3f97-9b7a-3fa0-9a10-d1cd4d56831a | -13.9251 | -54.627 | 2025-06-15 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 517d1810-e218-33ca-94ea-d47ea0cb04bd | -13.9254 | -54.6063 | 2025-06-15 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 245b319e-b79f-3310-b748-e094cd88ad6c | -21.26152 | -50.29891 | 2025-06-15 04:51:00 | NOAA-21 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8502c70c-1cef-34f8-9b4f-0fb8ad20c5e6 | -19.69783 | -54.61486 | 2025-06-15 04:51:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a8fc261-4929-3902-bf66-e1cd83a85e08 | -20.87165 | -49.07776 | 2025-06-15 04:51:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8abe36e8-2289-3ba1-b83d-0f76bed746e2 | -18.38404 | -55.73822 | 2025-06-15 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ae577524-57c4-3ecf-8293-06ae1a571ceb | -19.27199 | -55.14815 | 2025-06-15 04:51:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ffd9b29-eac0-306b-9225-7d8e1c9d0778 | -19.0233 | -57.62195 | 2025-06-15 04:51:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 97c3376d-ce97-308b-a523-497be1b04166 | -22.67642 | -42.85285 | 2025-06-15 04:51:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 70d95f38-5d8e-32bb-b045-a2d862fd12c5 | -20.47943 | -53.67718 | 2025-06-15 04:51:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b4d3f77-f03e-394a-b945-2cc3b83f3a2a | -20.41901 | -43.55545 | 2025-06-15 04:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 678bc914-39bc-3fe7-b2e1-bf41fb472237 | -19.69841 | -54.61121 | 2025-06-15 04:51:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e49b96d-1cee-3418-8c6b-92709c581a85 | -13.9251 | -54.627 | 2025-06-15 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 5309c1b0-4890-3069-84f8-fd1a07c130d6 | -13.9059 | -54.6291 | 2025-06-15 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| e9323ce4-5dc3-3f03-96b3-63bc9f631325 | -13.9062 | -54.6084 | 2025-06-15 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 153.7 |
| e4c568f4-125b-3fbc-982d-7884d82261a8 | -13.9065 | -54.5878 | 2025-06-15 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| f751dba6-64f8-3c7d-abe1-723cb913be43 | -13.9254 | -54.6063 | 2025-06-15 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 7f3f0ce5-d119-33fb-9cd5-523808d28315 | -13.9254 | -54.6063 | 2025-06-15 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 132.3 |
| ef526480-3d95-3676-abf0-2c3f57d49da2 | -13.9062 | -54.6084 | 2025-06-15 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 5366e631-ef8f-3f22-bfa0-ba763c650930 | -13.9059 | -54.6291 | 2025-06-15 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| fbd632a2-b2bb-3b0a-b78a-9640de105af5 | -13.9251 | -54.627 | 2025-06-15 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 52c88b27-fc8f-3fdb-af1e-352237947734 | -9.4119 | -48.43367 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 403b9b8b-548a-3c72-8088-c8c468577c04 | -9.41948 | -48.45236 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a295ec73-d1eb-3d74-afcb-93122741e456 | -9.41994 | -48.44874 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 42b60463-c9fb-3bc7-9c81-c31c94011be0 | -5.64258 | -44.10831 | 2025-06-15 05:12:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README12.md)
