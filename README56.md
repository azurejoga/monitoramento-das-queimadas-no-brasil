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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0c94520-3b3a-3144-ba29-a033361c3d70 | -6.32158 | -42.50812 | 2024-09-26 04:04:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b08c7b78-585e-369f-be06-d3f038666ecd | -6.31823 | -42.50761 | 2024-09-26 04:04:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 16392013-ddc0-3e12-ab00-8c6024da7d65 | -6.31487 | -42.50711 | 2024-09-26 04:04:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cad75ce7-4530-3494-9b47-3c9ec063df73 | -6.3143 | -42.51066 | 2024-09-26 04:04:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 639d310b-6cfb-3960-8a4e-d355ff617484 | -6.31095 | -42.51014 | 2024-09-26 04:04:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0ee4d226-f665-35ca-8eda-04140c789dde | -6.30311 | -42.41467 | 2024-09-26 04:04:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b3f2990-c49f-3bd3-8d85-512780a4a583 | -6.29977 | -42.41414 | 2024-09-26 04:04:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fb9e385f-1d7a-3304-9f61-8194191fbe4c | -6.2992 | -42.41772 | 2024-09-26 04:04:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6bcb8205-496e-360f-8821-17c9f4020d2d | -6.29586 | -42.4172 | 2024-09-26 04:04:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f07bcd5b-b982-3b7e-9eb7-b8e0089dcce9 | -6.2499 | -42.02149 | 2024-09-26 04:04:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 498bd3f0-8c54-3d61-af6b-31af0401301c | -6.03796 | -42.15968 | 2024-09-26 04:04:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 14ee5529-44bc-366f-a7e0-a6250e4a16e6 | -6.23715 | -43.3149 | 2024-09-26 04:04:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3eb9b4a-1508-3ba9-a7a7-ce1a487e52cb | -6.23655 | -43.31863 | 2024-09-26 04:04:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ee47271-0866-3141-85f0-19e43c10a5fb | -6.23372 | -43.31434 | 2024-09-26 04:04:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 278b756a-b1cf-3bca-964d-0bbe442b0e22 | -6.23312 | -43.31806 | 2024-09-26 04:04:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2abb83ec-bb59-39f0-80cd-5407ef412674 | -6.23029 | -43.31377 | 2024-09-26 04:04:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8cc3b20-9a48-312d-a132-df9a9c86cb30 | -6.22969 | -43.31749 | 2024-09-26 04:04:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecf0264d-7480-3487-ae55-99daaf84335d | -6.20545 | -43.27164 | 2024-09-26 04:04:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97e0eef4-12eb-33cc-aedf-3ba867a6df70 | -6.20485 | -43.27536 | 2024-09-26 04:04:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f23b30c-ddee-36b6-857a-ee564cc4553d | -3.53262 | -43.55522 | 2024-09-26 04:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 421e1a61-55e6-3e4c-9942-bc42b2c9e760 | -3.53199 | -43.55925 | 2024-09-26 04:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22da7f68-b676-3ea4-91c9-12c5be0c0927 | -3.5316 | -43.55773 | 2024-09-26 04:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed2d72fc-ead7-367d-aee1-ee7d350ed030 | -3.29915 | -43.51984 | 2024-09-26 04:04:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aab8704b-ffa1-3b6c-b021-daaeb4918b1a | -3.19939 | -43.89166 | 2024-09-26 04:04:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15da793e-6d17-3222-b231-e46c281136a0 | -4.80821 | -43.30237 | 2024-09-26 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb98ed96-5010-3621-a5ea-e21969544437 | -4.66552 | -43.7616 | 2024-09-26 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5318f283-5e44-3e84-8a12-6de73b8f7589 | -4.66262 | -43.75705 | 2024-09-26 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30c441e2-0d24-30b0-a650-6ff5d13eabd1 | -4.66198 | -43.76104 | 2024-09-26 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dccb2b6-1144-34be-aec1-e06e9b1fb906 | -4.65843 | -43.76049 | 2024-09-26 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f00c055-bade-3e0f-9103-586016c088e1 | -4.65779 | -43.7645 | 2024-09-26 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c71f020-9d33-3bca-a856-e526789741be | -4.65681 | -43.74792 | 2024-09-26 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cfe88ea-b21a-37e1-84e0-0814e59581f7 | -4.65326 | -43.74737 | 2024-09-26 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fb0aeb7-9ed3-3f00-aeb9-d82f43d0cc80 | -4.07373 | -43.38493 | 2024-09-26 04:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a507086-d311-3337-ba19-e9aaa30ad3bc | -4.07311 | -43.38884 | 2024-09-26 04:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ebd8786-91f9-375b-9919-7be0893436d4 | -4.81804 | -44.35336 | 2024-09-26 04:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65e2c953-61fc-3a24-b043-94010372d784 | -4.81771 | -44.35494 | 2024-09-26 04:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f3a1e39-b3f3-3f47-933a-c4bda774fca7 | -4.05814 | -44.0476 | 2024-09-26 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8abd3052-208d-394d-898a-e75a42173d32 | -4.05747 | -44.0518 | 2024-09-26 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c9a82358-9513-3f60-b5cf-940741dd69f6 | -5.98024 | -44.76165 | 2024-09-26 04:04:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89cbd5a5-94c8-3519-8cd8-de6b3bb82d07 | -5.96531 | -44.57684 | 2024-09-26 04:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86a4b1b0-8c0c-35fc-a5f0-0bf826b08f42 | -5.96464 | -44.58105 | 2024-09-26 04:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67ff5521-dd60-38b1-9d4b-4abcdbaabd09 | -5.96167 | -44.57626 | 2024-09-26 04:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e6ce953-49de-3e72-86d4-430190819687 | -5.71774 | -44.81351 | 2024-09-26 04:04:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0abfc9c7-efa9-3b92-be72-1c94555462f6 | -5.71704 | -44.81792 | 2024-09-26 04:04:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec5f2b0a-8659-38c7-b281-c35dbc682f39 | -5.716 | -44.81625 | 2024-09-26 04:04:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3fc696b-0cae-33e9-ad18-5cb1ff1bcc39 | -6.14079 | -43.86807 | 2024-09-26 04:04:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 736dfea8-f759-3cef-a317-4da5aff230a8 | -6.06603 | -44.03813 | 2024-09-26 04:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bb6dcb5-accb-38ed-8967-0d598edc15e5 | -6.06593 | -44.03948 | 2024-09-26 04:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4a07518-cfa3-31ba-9c62-341206959b35 | -5.8957 | -43.883 | 2024-09-26 04:04:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8afccfbd-2de8-3690-9f62-445e40f6bd36 | -5.89507 | -43.88689 | 2024-09-26 04:04:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0edf824b-8592-3467-b707-db2c17c75ca3 | -5.89218 | -43.88243 | 2024-09-26 04:04:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25a25223-3714-33f0-8dd4-79bc8068dd59 | -5.89155 | -43.88631 | 2024-09-26 04:04:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 96a5f2c6-ec93-393c-b684-06b5ad8b10c3 | -5.88866 | -43.88188 | 2024-09-26 04:04:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a3370ab-810b-3860-b534-4073f7400fda | -5.87177 | -43.75913 | 2024-09-26 04:04:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31cfab1c-200f-3753-98b9-e8923fe88545 | -5.6314 | -43.63445 | 2024-09-26 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4a11be6b-9e47-3548-abd0-6ce9af57eff4 | -5.62791 | -43.63388 | 2024-09-26 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2fad9223-b898-32f9-a345-f7c7c49d8b80 | -5.62729 | -43.63776 | 2024-09-26 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 895eebe9-66c0-3c32-ba31-4c301be67187 | -5.62603 | -43.64552 | 2024-09-26 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb1d888c-8d14-3e85-895e-fb8aec738f4c | -5.62505 | -43.62944 | 2024-09-26 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8ac0a35-08ca-3da4-b85c-c390edbf3364 | -5.62442 | -43.63332 | 2024-09-26 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4a36a148-0830-3989-9131-59ca849dac54 | -5.60634 | -43.63441 | 2024-09-26 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e3a2ff4-247c-3180-9d67-d2f144754a1f | -5.91387 | -44.01653 | 2024-09-26 04:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4640179-b0e8-3369-9d4c-9de91e5a11a4 | -5.91033 | -44.01596 | 2024-09-26 04:04:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9750110e-f7a6-39a8-b960-f806b8c7a580 | -5.87588 | -44.13857 | 2024-09-26 04:04:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 752826d7-e1ca-3dfd-9863-a5cae002d6c5 | -5.86296 | -44.12815 | 2024-09-26 04:04:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64daab93-3998-3c76-88a6-8fde1dd2791c | -5.86231 | -44.13216 | 2024-09-26 04:04:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1a6402b-9a54-3a8d-8476-646dc727ff93 | -5.85874 | -44.13158 | 2024-09-26 04:04:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41cbc86f-ff12-3d87-a23e-6ba783176a16 | -5.79503 | -44.147 | 2024-09-26 04:04:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 16f8f382-03f2-3223-8b2f-d723013f0a60 | -5.74073 | -44.00986 | 2024-09-26 04:04:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b43151fc-5773-3db1-864c-3cb98eba7265 | -5.72639 | -44.32082 | 2024-09-26 04:04:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 760b854b-ed2b-3edd-934d-f5d5b281a2dd | -5.59003 | -44.07058 | 2024-09-26 04:04:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbb808b7-b302-3256-9e83-b8981c1d47a9 | -5.57951 | -44.41846 | 2024-09-26 04:04:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4812b05f-1cb2-3706-86c4-f6154b0eee81 | -5.57589 | -44.41786 | 2024-09-26 04:04:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c72db9a7-0bad-3e4d-ade5-a1bd72628b84 | -5.56433 | -44.42028 | 2024-09-26 04:04:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4ef7f08-2802-321f-9564-b111332aacc1 | -5.56321 | -44.4219 | 2024-09-26 04:04:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dee4c38d-cdc3-333c-88c9-2db404f3187f | -5.09594 | -45.2109 | 2024-09-26 04:04:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| afeab3c3-aca3-3b9b-878f-593f5d7ad3b1 | -5.09519 | -45.21559 | 2024-09-26 04:04:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 776b86b1-08e0-3f0e-a48d-7729861e550f | -5.09212 | -45.21035 | 2024-09-26 04:04:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c0cb370b-281b-3855-accc-9794b69c5095 | -5.09137 | -45.21505 | 2024-09-26 04:04:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a3a5ecec-22b6-3d21-9459-8cdd287f30b2 | -4.58513 | -45.689 | 2024-09-26 04:04:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f500a422-31fb-3695-bcc1-c85691b3262a | -4.58429 | -45.69423 | 2024-09-26 04:04:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da68d4a9-e05f-37f9-ae0f-73024ea3846e | -4.58034 | -45.69352 | 2024-09-26 04:04:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d116a875-8f14-3c8c-bff9-8c12a1b3067e | -4.57639 | -45.69287 | 2024-09-26 04:04:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d299cd33-bcee-3a2c-8b85-c29501ffccae | -4.51878 | -45.57508 | 2024-09-26 04:04:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69fdf4a1-db7e-3008-9a78-6fb9964e9240 | -4.501 | -45.90459 | 2024-09-26 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 55c0cf46-fe78-3ca3-9efa-a9e17c4abdf4 | -4.49699 | -45.90389 | 2024-09-26 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46759a0d-77a5-3c41-9d6b-aeee507d42c0 | -4.42728 | -46.09949 | 2024-09-26 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00e4d5df-8e7e-3b97-bab1-6ab5e27b32a8 | -5.54785 | -45.10051 | 2024-09-26 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc1cffe2-6d8c-39cb-9fb3-d2be7dec904b | -5.54712 | -45.10509 | 2024-09-26 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 610ec46e-788f-3e19-96e5-55e3d98651b4 | -5.53257 | -45.34098 | 2024-09-26 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9efbac3f-08b4-32d0-91c8-235b231e9731 | -5.53174 | -45.33819 | 2024-09-26 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9885a33b-307b-386e-8a00-cf9d7e229b42 | -5.53007 | -45.80627 | 2024-09-26 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2ea00f3-05a6-3082-aa7d-08d4bfd2c040 | -5.49196 | -46.37096 | 2024-09-26 04:04:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54157f6b-fe4d-3513-8bfa-839777aa556d | -5.47126 | -45.86869 | 2024-09-26 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5018c954-100c-36e3-9d4d-8efd2ed5b128 | -5.4704 | -45.87384 | 2024-09-26 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be91fb0c-2b58-3448-bccf-f8e6bb36924e | -1.17041 | -46.86523 | 2024-09-26 04:04:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0731869a-34bd-3439-b2e2-6a93a63b4926 | -1.16773 | -46.8625 | 2024-09-26 04:04:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 705cd085-8774-3e42-96a5-caca7319a815 | -3.32484 | -47.01635 | 2024-09-26 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e54985da-251e-3c1f-97d7-731e1d4f42d4 | -2.73061 | -46.76222 | 2024-09-26 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f374fd2-c036-3e18-85ae-71296a884cc1 | -2.72992 | -46.76646 | 2024-09-26 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README57.md)
