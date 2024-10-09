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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ea3dda2-9e96-389d-b4c4-f021b48096d2 | -21.62684 | -44.62827 | 2024-10-09 04:17:00 | NOAA-21 | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4b4c3825-6984-3eaa-af46-81fd9b26c8c4 | -21.62626 | -44.63228 | 2024-10-09 04:17:00 | NOAA-21 | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7be2da30-e31c-3c21-9869-8696fcde5063 | -21.62569 | -44.63626 | 2024-10-09 04:17:00 | NOAA-21 | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8ceb84a4-b243-3a3f-b8c2-6682e0be9a43 | -21.62341 | -44.6278 | 2024-10-09 04:17:00 | NOAA-21 | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c779d907-20de-3807-8de9-400bc7239a37 | -21.54756 | -44.15237 | 2024-10-09 04:17:00 | NOAA-21 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 27e42242-2669-3410-af41-f80540bdbf5d | -13.8781 | -44.52719 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 982c81fa-fa7b-3062-adb2-902cc15ff24a | -13.83843 | -44.58258 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3dfbde5-48a7-3283-904f-24502048c844 | -9.43242 | -44.12694 | 2024-10-09 04:17:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4f388db-0fbf-3a82-a284-4093ba0b7451 | -9.9484 | -44.11448 | 2024-10-09 04:17:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6abbac11-3635-312c-a645-69add7883748 | -9.9451 | -44.11396 | 2024-10-09 04:17:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 486dabb5-5d76-3bf3-86f4-1d2f7e6ae750 | -9.93685 | -44.10193 | 2024-10-09 04:17:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8d41bd5-8384-3d3e-9963-aebe970ced8c | -9.93518 | -44.06957 | 2024-10-09 04:17:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0823e7a-1a0c-3895-b394-41ea247db796 | -9.50381 | -44.06413 | 2024-10-09 04:17:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99f498a8-7be4-345d-bafa-6bf5ef1894ca | -13.37637 | -43.76855 | 2024-10-09 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d8040c2-579c-31a1-af24-01f092cb1b93 | -9.43188 | -44.13042 | 2024-10-09 04:17:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0c54110-8407-3c4a-883c-b3d26775517f | -9.42858 | -44.12989 | 2024-10-09 04:17:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ad46ffc-f442-3d8a-a47d-17b06c481836 | -9.42692 | -44.11897 | 2024-10-09 04:17:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34b584c2-fab3-3308-a03d-887f81efee42 | -9.42361 | -44.11844 | 2024-10-09 04:17:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1758763-626f-35ab-990e-3de5bf35185c | -9.41537 | -44.12782 | 2024-10-09 04:17:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dbd2f29e-4ea6-30a0-b06b-878366e69d39 | -10.15718 | -43.80182 | 2024-10-09 04:17:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b33ff1a1-1a5d-30a1-b33c-f64ee1e865a3 | -10.56745 | -43.72479 | 2024-10-09 04:17:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c054c974-1b9c-3149-908b-bad4593d7c3d | -11.9283 | -44.61561 | 2024-10-09 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 018b9e73-ed1c-349e-9b2f-fd1d72df695a | -11.925 | -44.61507 | 2024-10-09 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f568c383-29b5-393e-8603-6c4df93d6d6a | -11.92445 | -44.61858 | 2024-10-09 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d96f1214-a0d0-3c22-a050-71fd1f4911b6 | -11.8932 | -43.88412 | 2024-10-09 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 557a1a84-70ec-38cc-a0ae-4e9a9ae07be8 | -11.79351 | -44.50034 | 2024-10-09 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 808946c2-21f9-3774-84b7-149c317bdd5a | -11.79296 | -44.50385 | 2024-10-09 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0eeefed8-32b3-3939-a6e8-24ce0753c10e | -11.78208 | -44.5266 | 2024-10-09 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b5abb72-25f9-3d98-b7b6-ee4bee3a4559 | -11.78152 | -44.53011 | 2024-10-09 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb89488a-5066-39ef-9963-28f65b4f56c7 | -11.73973 | -44.49462 | 2024-10-09 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 63c73a0f-3d7a-3f8b-9fc3-7544492ddf5f | -11.73918 | -44.49812 | 2024-10-09 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 83c7ee93-d1f5-30e6-bef2-5e35a937d939 | -12.03976 | -43.94719 | 2024-10-09 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 766894b4-9f84-383f-a0dd-43d6f71120fc | -11.89265 | -43.88764 | 2024-10-09 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 140e1209-45ab-3b03-bab8-abaeb4627234 | -10.84576 | -44.38163 | 2024-10-09 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daecbded-7f89-32fb-96e6-936a28af44d9 | -11.88934 | -43.88711 | 2024-10-09 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bafdce4d-ebee-32b4-bf93-b1897c5b49ab | -11.76611 | -44.219 | 2024-10-09 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95204177-dd9c-335e-8d3b-22a3b35d5f24 | -12.87055 | -44.61884 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b4331f5f-6f01-3b53-bc76-4806c2725f17 | -12.86725 | -44.6183 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 46457b14-5b09-3a0d-b75b-6b57f88523c0 | -13.74924 | -44.01873 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8a9ef9b-fa6e-3718-b5ac-6d0c10a4d4a2 | -13.71804 | -44.24332 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aabe1ee9-6a82-3354-80eb-73f7e7da3d50 | -13.3764 | -43.79058 | 2024-10-09 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b160a00a-188d-325a-be0e-eba9f8a159b7 | -13.37585 | -43.79416 | 2024-10-09 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f006599b-7fb5-3c55-8df6-3599c6a635a8 | -13.37304 | -43.76802 | 2024-10-09 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b456e0d5-1a19-3079-91b1-c306a8f34c85 | -12.87708 | -44.61995 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e30011a4-5175-3616-922a-8dcc070ebb95 | -13.51491 | -44.0617 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13eba87d-e20c-3521-80eb-8f415218c440 | -13.4168 | -43.72728 | 2024-10-09 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf348e7f-fed8-3faf-9734-e39b7abfce0f | -13.57305 | -43.74854 | 2024-10-09 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94f1eb3b-da87-3598-8d34-c29835933613 | -12.65663 | -44.24524 | 2024-10-09 04:17:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe2038c2-e993-35c0-9a7c-6272dd9b3a25 | -12.57474 | -43.36567 | 2024-10-09 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74e9575c-df5d-3adf-a9e8-eda1b3169418 | -13.76193 | -44.00248 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca87d314-368e-34f0-888b-8653c665f734 | -13.73429 | -44.00534 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da5ae3d4-ada1-3ca0-9265-c9c64cad6d97 | -13.42296 | -43.79805 | 2024-10-09 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 622fe06b-455d-3a2f-90b7-56c5310e1533 | -13.33356 | -43.71392 | 2024-10-09 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cee3b4eb-8ce1-3fdd-8ab9-dbcc2660ccfc | -12.78157 | -43.41323 | 2024-10-09 04:17:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88796a5c-ba48-3e4f-9934-c39b5d0b38c3 | -12.78102 | -43.41684 | 2024-10-09 04:17:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 643698f8-1cd6-367c-92e7-8ee3467c6a42 | -13.36929 | -44.77631 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b553c56-1123-3782-95fe-909d566904dc | -13.36873 | -44.77983 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09c7d79e-f341-3413-85d8-5c6c0760aae4 | -12.88149 | -44.61345 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35dedf75-1af6-3e84-a37a-8acbfeef5751 | -12.8733 | -44.62289 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00112e18-b40e-38f1-ac37-39926c321d98 | -12.86781 | -44.61479 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| feced8f1-2f5c-33d7-87ec-c77132bdc3cb | -12.77951 | -44.8924 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 371253fb-5dd4-3aae-bc1f-5cde7f1de2e5 | -12.77895 | -44.89592 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1de84861-68f5-37d2-a769-c108d7b5d270 | -12.77839 | -44.89944 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bbc2338-c3aa-38db-bc61-f2ebf607632d | -12.77621 | -44.89185 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01977c56-00da-3b02-8262-3a0ff7387533 | -12.3656 | -44.73373 | 2024-10-09 04:17:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b7997c4-6a3c-37b6-adfe-1071e5c101f9 | -13.83733 | -44.58963 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a5443caa-7be5-328d-85ef-c4138bac6b61 | -12.36505 | -44.73724 | 2024-10-09 04:17:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7839a51-6857-33cd-8a3c-eb4af386920e | -12.3623 | -44.7332 | 2024-10-09 04:17:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d106af8a-83d8-3222-ae2c-ddc1fd49108b | -12.36174 | -44.73671 | 2024-10-09 04:17:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 179ea78d-e428-34c0-bdb0-4f8edee44771 | -12.35844 | -44.73616 | 2024-10-09 04:17:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b03a2eb-38fb-3d24-9a37-5f5b0163e42a | -12.28568 | -44.80729 | 2024-10-09 04:17:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9dfdb63c-abd9-3f96-9823-ddfa8e911633 | -12.88094 | -44.61697 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca296c5d-6ee7-34ef-8839-1b42df0b1849 | -12.87 | -44.62236 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 616c1ccd-fcfc-33ee-a181-9471c37ba623 | -14.11033 | -44.97509 | 2024-10-09 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6003643e-099d-3207-9482-7d275c07334c | -14.51225 | -43.84938 | 2024-10-09 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc1aeae8-f109-393b-a7c4-f9b97379f92c | -14.51171 | -43.853 | 2024-10-09 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 803d803e-1679-3d20-9722-758128fb3ccb | -14.51116 | -43.85663 | 2024-10-09 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e087fcad-44ba-3230-a74b-918e07e0774d | -14.50891 | -43.84884 | 2024-10-09 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90637c69-f485-3bd2-ac5f-6c2cc03c8ad7 | -13.84173 | -44.58311 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4766a6cd-db29-36c1-bb02-fa92e09dc81c | -14.50837 | -43.85247 | 2024-10-09 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fcefd5a-9b75-3ed0-8f4a-d576cd489977 | -14.50782 | -43.85609 | 2024-10-09 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6daa346-7392-37d7-b181-8cc4d398491d | -14.27061 | -44.18673 | 2024-10-09 04:17:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 292b34b4-3ee4-338b-a5f5-b646c1101073 | -14.11197 | -43.71139 | 2024-10-09 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 434961a1-061a-34a4-839a-0414e385d239 | -14.10019 | -43.96833 | 2024-10-09 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ad7f963-6096-39a6-9d6d-09a6333932bc | -14.08875 | -44.15359 | 2024-10-09 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 195aa6dc-8859-3bc6-b9c1-9ed8d8f4a99d | -14.08599 | -44.14948 | 2024-10-09 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cfe53eae-2899-3582-8d23-e8768848ea7b | -14.08544 | -44.15305 | 2024-10-09 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f42d26c0-91e9-3d88-ac00-a7b39897064d | -14.08428 | -44.09427 | 2024-10-09 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac5746a2-58e7-30bb-89fb-f5a5c360f274 | -13.89943 | -44.28012 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14fa5871-b72c-398f-ad78-2133efe5d328 | -13.89758 | -43.80379 | 2024-10-09 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b01a84bf-a37d-3c35-a2a1-7d24262fa54a | -13.89667 | -44.27604 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 186ed29e-f1ed-37ec-8822-1d433071e49f | -13.8682 | -44.54731 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 900a7563-73fc-3c99-8e86-d1949400ffeb | -13.86214 | -44.5427 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ccf6cac2-31a2-3052-8d3f-5e2797f82a3a | -13.85884 | -44.5639 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4521cae3-564d-36ef-8529-902852445e73 | -13.85829 | -44.5457 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d51410f2-4f04-35e2-83c4-a182c7ffa32d | -13.84339 | -44.57252 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a11c0082-72c3-3780-accc-2e0566523851 | -13.84228 | -44.57958 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 316de90e-8600-3cb9-8076-243afa34bfe4 | -13.83568 | -44.57851 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 225b931f-33a5-372f-b9e1-3b98597766ed | -13.83513 | -44.58204 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36bca076-73d1-3ed6-819e-aaa0f4e8ceb3 | -13.82687 | -44.59155 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README85.md)
