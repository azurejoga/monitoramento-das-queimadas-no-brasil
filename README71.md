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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aed32e4b-25dc-38d1-8c12-cf8f9055ce85 | -6.07698 | -48.05592 | 2024-12-02 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0061b736-9d41-3bb3-94c0-137347371cf0 | -11.06005 | -45.37955 | 2024-12-02 04:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 903846a4-3ea8-36f1-8a89-76525883be7b | -6.08472 | -48.05708 | 2024-12-02 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3c6b6f94-3e32-3eef-968a-ace5f04441fd | -6.08086 | -48.05649 | 2024-12-02 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9753bcb7-cf5d-35a0-9df5-fe28e2a14fe5 | -9.34464 | -58.22872 | 2024-12-02 04:50:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9890095f-ab75-3e2c-ae95-99a6b00a0b54 | -6.74388 | -48.77299 | 2024-12-02 04:50:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ff52f58-5878-396a-aa68-7eeeb104f0f2 | -6.46023 | -47.54261 | 2024-12-02 04:50:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64f4649c-1dfd-3fe4-a059-2816626de275 | -11.06124 | -45.37572 | 2024-12-02 04:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fd5eac6-66ab-3631-a931-ddf4bb7f438e | -5.60993 | -45.06084 | 2024-12-02 04:50:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5971648-e8ef-38e1-8eb1-093e4f77ff62 | -6.36697 | -47.35361 | 2024-12-02 04:50:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecfda1ea-6297-363e-b9bf-f7696b1b7c6d | -6.40319 | -47.21786 | 2024-12-02 04:50:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 102a52f9-d185-3730-89e0-81bdf42444e5 | -17.4784 | -51.82727 | 2024-12-02 04:53:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93c01f74-acc0-3255-b407-39057fe0192e | -15.09086 | -59.63571 | 2024-12-02 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a71ce13-ea54-3a13-a25a-38dccb2f1eef | -13.47774 | -56.55706 | 2024-12-02 04:53:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86c5ebb7-3de7-3e13-8134-d189c591be18 | -12.38241 | -63.67864 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9228dc33-2c06-38c2-94ff-ab63ca150186 | -19.72897 | -49.63871 | 2024-12-02 04:53:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5618e3ee-e243-356b-8042-5d9d92f59abf | -12.42639 | -63.74487 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e8d3b365-0283-3225-b2a6-993d4ce1e08d | -16.01433 | -58.46317 | 2024-12-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1d84bf03-4946-3365-bb02-e662fabf988e | -12.87844 | -60.00346 | 2024-12-02 04:53:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80c1d727-94c1-34c5-a164-e74bfcc40885 | -13.50115 | -61.53775 | 2024-12-02 04:53:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba06d094-8d6b-3154-b9be-05ec6d1b3531 | -11.81421 | -61.73067 | 2024-12-02 04:53:00 | NOAA-20 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 120e6653-949b-319e-a1b3-b560cf2700a9 | -16.67928 | -43.88403 | 2024-12-02 04:53:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c60b074-8139-34e5-8016-0350dca41205 | -15.06758 | -59.64986 | 2024-12-02 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44446449-b8d4-390d-9ee9-975065cebef9 | -11.8132 | -61.73615 | 2024-12-02 04:53:00 | NOAA-20 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c051afa8-6286-3a2b-ac48-719d612ebdcb | -12.43256 | -63.74236 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5ef09ef-8ace-3843-a4f3-f27e6a9ed283 | -12.25295 | -60.51193 | 2024-12-02 04:53:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03a3d11f-ef34-318e-b3ac-d6234ba95ac4 | -12.43268 | -63.74279 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e9b26ef-1518-31b1-8668-798747f6f32d | -12.42648 | -63.74532 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ef00d6be-0b39-3f5d-883d-c3d43005d532 | -12.41955 | -63.7515 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8760372e-1ce2-3c41-90c4-f3cca7052e8e | -13.5058 | -61.53869 | 2024-12-02 04:53:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1858a11-9898-39b0-9d26-f51a9f8646f0 | -12.59099 | -54.37951 | 2024-12-02 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 12ead174-6e94-347a-84b9-3a687aa012fd | -21.77267 | -57.34753 | 2024-12-02 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 612ea79f-732d-3b1b-8fba-8f90da9ec03e | -12.38312 | -63.675 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb8acf00-46e6-3b92-a1f0-7b8c5136be26 | -12.59431 | -54.38005 | 2024-12-02 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e14e4b13-601d-3cac-a898-2db6891f10a9 | -12.43195 | -63.74644 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 68211bc0-f56e-36d0-a79f-e6466b8d062d | -12.42569 | -63.74855 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6cb19621-7054-3871-b5d6-733efa73f580 | -12.42575 | -63.74898 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9a0acde7-b4f9-31b8-ad42-c575e9c0b2c6 | -19.0217 | -57.62312 | 2024-12-02 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f3f1b665-335a-30ff-aa9b-4c7ac0e4376b | -12.24624 | -63.4677 | 2024-12-02 04:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7f13c07-9272-3fb1-a8be-a8700cf0ffd2 | -12.42499 | -63.75221 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e00acdba-b40e-300a-b2ab-387a696bfc2d | -12.24692 | -63.46417 | 2024-12-02 04:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d15322e0-d56e-3284-a34d-0d3d9893c356 | -13.50207 | -61.53274 | 2024-12-02 04:53:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3bee098b-e09b-3952-b40a-07663cb664fc | -12.41475 | -63.74625 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7acda901-3850-3f39-93c9-7460022712fd | -12.25229 | -63.46539 | 2024-12-02 04:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 144417d2-6369-3812-b127-508655c5bf89 | -12.43122 | -63.75011 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b7ec47cc-dd90-3499-b088-9fd3d23fc976 | -12.42028 | -63.74786 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f1ba620a-9552-34ba-b1a6-0cbc3468c5a9 | -13.50349 | -61.53959 | 2024-12-02 04:53:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55494013-b621-3f50-af10-fa22e234e1b5 | -12.42502 | -63.75264 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8556ecfa-ff39-3d26-bfff-5359fa96489e | -13.50445 | -61.53458 | 2024-12-02 04:53:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c87a669-bb2c-3e14-af09-79e45ac3c5ac | -17.47779 | -51.83156 | 2024-12-02 04:53:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81f37a45-555c-335a-aac6-e0792887f45f | -15.07159 | -59.65061 | 2024-12-02 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d9d2ad0-1c3c-32fc-9461-0323816f6ef4 | -12.43186 | -63.74602 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 44ebfa27-7861-3391-b5dd-56177c10fdb8 | -12.41545 | -63.7426 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0643a749-744f-3ac5-a086-134f9d67a716 | -12.42101 | -63.7442 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5c802f6e-3861-3a4a-84f5-4902b9dc35fc | -12.41405 | -63.74989 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f087a6db-2126-3f39-8120-fa918fbc2ab4 | -12.41952 | -63.75105 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba9a578a-9971-3288-ba55-98b29e27e598 | -15.09486 | -59.63651 | 2024-12-02 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3c19cf47-7681-3ac7-9f12-abd597c4783f | -12.4169 | -54.74456 | 2024-12-02 04:53:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11def292-ae04-3976-8e8d-d14731020c08 | -12.43116 | -63.74968 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f5485fab-310b-3313-9619-59b6daa10bbc | -19.72926 | -49.63684 | 2024-12-02 04:53:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4272ebd5-a1e6-3660-8cfc-145b924e8a76 | -12.42022 | -63.74741 | 2024-12-02 04:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11beab47-71bb-332e-b3a2-525364afda38 | -20.72281 | -54.42823 | 2024-12-02 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 516740df-5700-3458-88ae-47da37062401 | -20.72675 | -54.42496 | 2024-12-02 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b21f065a-e2c1-36e3-bed5-3cbf4ce76f97 | -19.50399 | -56.60713 | 2024-12-02 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 78fafe20-6112-3d4c-9268-339dded1e23b | -20.72224 | -54.43206 | 2024-12-02 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04656f1a-b846-36a0-a5ce-74db8f506474 | -20.72167 | -54.4359 | 2024-12-02 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5e968c1-6324-3d28-9f06-c3bf111e57b8 | -20.72618 | -54.42879 | 2024-12-02 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 074e9fd7-874b-3f63-983c-4b1353f6635d | -21.20143 | -56.91384 | 2024-12-02 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19b56eb3-31e3-33cd-bde7-d879ae230075 | -20.73121 | -54.94422 | 2024-12-02 04:55:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e03a818-b960-396a-9735-ec661d8008ee | -22.55504 | -43.55117 | 2024-12-02 04:55:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 97628d84-73d2-348a-9b5d-c93b3ff53b56 | -22.7166 | -48.23682 | 2024-12-02 04:55:00 | NOAA-20 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3b5db8fc-32f4-3e04-a726-0dad57c3ebb4 | -5.1181 | -43.1964 | 2024-12-02 05:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| e8b49343-2214-3470-8623-48b70ce4f22e | -3.259 | -53.6388 | 2024-12-02 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 93d6e4d4-7251-3cec-bd90-e55c17d89a23 | -3.2591 | -53.6186 | 2024-12-02 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8d6c3c5a-cb3d-3b45-a0a6-22995a9c0552 | -12.4358 | -63.7455 | 2024-12-02 05:00:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e5e5d6b3-2779-3a2e-8c71-6c51b00f9389 | -3.2708 | -46.4511 | 2024-12-02 05:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 6357ec4b-4029-37c5-b90b-0e98ca5a8f9f | -2.5612 | -53.3931 | 2024-12-02 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| ffb3129c-438a-3bb1-b66d-34fc07e7f8c2 | -2.5428 | -53.4137 | 2024-12-02 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 933fc879-8e6d-3445-9573-c4ac91204d03 | -2.5612 | -53.4133 | 2024-12-02 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| cdefbf4c-c506-348a-96ef-8bfbed4045f8 | -5.5882 | -45.1412 | 2024-12-02 05:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| b81688a8-480d-30f0-87d6-a35d573cedff | 1.1072 | -56.007 | 2024-12-02 05:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 6caab73c-d6b2-350e-978b-30d4eaaebcb8 | 1.0889 | -56.0072 | 2024-12-02 05:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| ae60d5fe-2629-3927-a03d-a7e6910f3acf | -5.118 | -43.2198 | 2024-12-02 05:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 0cd8d5c7-3ffb-3b8f-ba92-43ab1a3307d5 | -5.5882 | -45.1412 | 2024-12-02 05:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| fbee6085-21f7-3b2a-ac96-35049a71fe60 | -3.259 | -53.6388 | 2024-12-02 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 57517fc7-f966-308f-bb84-fcde583435ec | 1.1072 | -56.007 | 2024-12-02 05:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 8028d509-9a42-3327-93c8-7fc610754d16 | -5.1181 | -43.1964 | 2024-12-02 05:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 54078da9-f216-3b88-bba5-e0ebaca0b347 | -3.2591 | -53.6186 | 2024-12-02 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| be98701b-c673-35ef-b59c-f6a78c03a0af | -3.2708 | -46.4511 | 2024-12-02 05:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 9eefe8e9-aab2-3b8d-9eac-75d888063288 | 1.0889 | -56.0269 | 2024-12-02 05:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| d6db63b1-3053-3066-8ec9-95ff13e8d55d | -5.118 | -43.2198 | 2024-12-02 05:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 2df2ad4d-3654-3982-b548-c3425afa067f | -5.5882 | -45.1412 | 2024-12-02 05:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c470b7c1-c8de-3fde-8288-bd10d1b460e9 | -3.2591 | -53.6186 | 2024-12-02 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 8070929f-5d2f-3626-9fd1-9f1174b9a4d7 | -3.7812 | -52.0335 | 2024-12-02 05:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 3aaf6303-d157-3d0b-bc25-8722f8cbcbb3 | -3.259 | -53.6388 | 2024-12-02 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| ec77ad09-bf64-3d49-94ad-8c3c18956edc | -3.259 | -53.6388 | 2024-12-02 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 00b088dd-5c1e-3678-afab-1e750a952e1f | -5.5882 | -45.1412 | 2024-12-02 05:30:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| b9ba75a0-80af-3ad1-983d-8211cd48637e | -3.2591 | -53.6186 | 2024-12-02 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a25f5f61-a724-393b-a24e-11070b6d4b80 | -3.2591 | -53.6186 | 2024-12-02 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 7dbf39ed-5356-3728-81da-0cf050feb566 | -3.259 | -53.6388 | 2024-12-02 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |


[Clique aqui para ver as próximas entradas](README72.md)
