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

## Dados Diários - Página 170

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b05af55-7f63-33f5-b06b-c32257855086 | -5.70057 | -43.90257 | 2024-10-25 16:52:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 8a11e61e-efec-30c6-9ba9-b9b362a6cad2 | -5.56216 | -43.77676 | 2024-10-25 16:52:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 950c97d7-c921-3a5b-a8f4-4e1026826ff0 | -5.56141 | -43.77218 | 2024-10-25 16:52:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3bbf7924-97e9-31fc-aa40-a0f5fbfb1082 | -5.98998 | -44.42667 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f16a689f-4a21-3e42-8796-5bfccb0e6813 | -5.97025 | -44.2249 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6208284c-ad98-3f45-945c-ca6e47860264 | -5.94263 | -44.95584 | 2024-10-25 16:52:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 479dfa1e-b351-37f4-9e37-1665b7c7a0b4 | -5.94199 | -44.95198 | 2024-10-25 16:52:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 331f8fbb-2bfb-3cb8-b4c7-78d27fc9013f | -5.93281 | -44.65818 | 2024-10-25 16:52:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 65f4c05c-afbd-3bc1-bd06-6a1cf0a547e3 | -5.90417 | -44.80236 | 2024-10-25 16:52:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 82ef6750-20af-3dab-a258-4cd53bbc6b30 | -5.89354 | -44.28039 | 2024-10-25 16:52:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 222b579c-ed6c-31fb-87d7-0dbe7839cc51 | -5.89339 | -44.27811 | 2024-10-25 16:52:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 09ef5a93-472a-3935-9b60-d75d57820f04 | -5.8912 | -44.15846 | 2024-10-25 16:52:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5fa1b05e-5767-3d77-94d1-23d6058746c6 | -5.8868 | -44.15931 | 2024-10-25 16:52:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0f6e8219-1d68-3090-a462-51afc87e85bf | -5.82345 | -44.89197 | 2024-10-25 16:52:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c956a88-e8b0-3c80-bbe7-bb9402092dd9 | -5.82282 | -44.88816 | 2024-10-25 16:52:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 721cf304-e18c-3107-8a3b-17b31f53feee | -5.80905 | -44.07016 | 2024-10-25 16:52:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f1c1bf4f-a33e-381e-b020-0d9dee2c8478 | -5.79548 | -44.82806 | 2024-10-25 16:52:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bbd21823-12f4-3209-a32d-e24c2ee71583 | -5.79299 | -44.91686 | 2024-10-25 16:52:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 38c23ba3-2f41-319e-b401-69045c1f8273 | -5.7199 | -44.02023 | 2024-10-25 16:52:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7e63202c-fb6a-3a72-a533-3f12aa08dd07 | -6.27652 | -43.81709 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| adfad6ef-fe95-3984-b52e-0995a7b60d9a | -5.62656 | -44.83016 | 2024-10-25 16:52:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 61c97bde-be55-3a8b-94fc-462cc8fb5d72 | -5.58128 | -44.25088 | 2024-10-25 16:52:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7b19cae5-5e6e-32e7-9993-818992ff10dd | -5.57024 | -44.88442 | 2024-10-25 16:52:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| ceea2ece-a880-3c12-b632-2b382ccb3a72 | -5.5435 | -44.10849 | 2024-10-25 16:52:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4486d33e-c190-3cd7-8c87-e7a5e661d285 | -5.53903 | -44.10918 | 2024-10-25 16:52:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 52b8b60b-8b23-3394-b2c0-ed2d92e87dfd | -5.42972 | -44.79207 | 2024-10-25 16:52:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| aad83865-1d7e-38f7-acd5-ec8fca3fe61b | -5.42873 | -44.79227 | 2024-10-25 16:52:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ee3de397-5129-3ca5-92ae-56326bcd8b6c | -5.35366 | -44.48708 | 2024-10-25 16:52:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cb3c29b7-5ca2-3382-a6bd-1d8f791c2886 | -5.12084 | -43.84191 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2ee9dd14-ee73-3507-9296-5b2ffc0994cc | -5.11707 | -43.84756 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a7e69428-ecce-331d-8ead-30de876e5c05 | -5.11629 | -43.84283 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4958cac0-6377-3d3c-9da1-c4b311ea7dd2 | -5.11331 | -43.85323 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 322000cc-603a-34eb-a685-32a2d643ce65 | -5.11253 | -43.84851 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b7e6309d-d3c9-3337-9de1-88d2267c2957 | -5.11174 | -43.84377 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 12ba4fbf-090b-3b25-86f7-efda8285e0ba | -5.10877 | -43.85417 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 2891f638-138c-3cad-bd1a-021059c61cd7 | -5.10799 | -43.84949 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0857c0b3-4c5b-35d8-8d6f-1b227ae0b2fd | -5.10719 | -43.84473 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e265dd0d-5d93-3687-a19e-b2964292906b | -5.1995 | -44.79062 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d58d7f0a-392f-3ae2-a08b-4602903a6d4e | -5.05654 | -44.76802 | 2024-10-25 16:52:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 78409a6d-f9a2-325d-9335-87622edc404b | -6.56055 | -43.91547 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0d1b0636-9b38-378f-8241-d6b5790e1ac5 | -6.52176 | -43.79333 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b97a3872-1cc6-330d-9e5c-fdd4df8d2c0c | -6.50576 | -43.99624 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e6b4bb87-d084-3faa-b648-f285837920eb | -6.49959 | -43.90668 | 2024-10-25 16:52:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bb868ea4-2843-3dd4-8430-06d0ef7c4ea0 | -6.47427 | -43.89274 | 2024-10-25 16:52:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 483c20f5-acfe-3e45-8008-75a08f2eb25b | -6.47106 | -43.8908 | 2024-10-25 16:52:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3d47d68d-a98f-3760-af24-adef6e4111ee | -6.46982 | -43.89353 | 2024-10-25 16:52:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e8ef31c-c266-3f1b-9f13-bf53e6dc44c9 | -6.33195 | -43.78897 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8300d851-c165-3e1d-be27-8272cfa57848 | -6.32745 | -43.78975 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 05ab878a-f370-3408-966e-27ad3bb39be1 | -6.281 | -43.81624 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 92f283eb-6d24-32b1-8169-7b590487b1a8 | -6.14526 | -43.80225 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 5805db19-cf0d-31e0-9d67-b9bbdb1aca68 | -6.1429 | -43.8052 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1786e77d-d5a8-3030-ae7a-a243e2bff4da | -6.13743 | -43.6641 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 03aea831-4c56-38e6-9946-09367ba3611a | -6.13288 | -43.66491 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9f920965-0b25-364e-97ab-7722c81f693e | -6.05536 | -43.90104 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fef2732d-9345-3a2c-a335-b0c9ef16558c | -6.05368 | -43.90449 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 204a291a-1bc6-3f8f-bddd-c761ff42d3ef | -6.05296 | -43.90004 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 892d57f2-52ad-3817-bb1c-65b3a1df4dde | -6.05087 | -43.9018 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 34a66b55-fde5-38b5-81ab-282894edb435 | -6.51545 | -44.18821 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6f4cc0de-1a93-3eba-b751-40d9aa77cd34 | -6.4898 | -44.03233 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1e3da080-ebe8-3b19-bed2-3f9a06c0f7e1 | -6.46392 | -44.09481 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 40dc4ca0-311a-32a4-8e3e-74fd71820184 | -6.45953 | -44.09559 | 2024-10-25 16:52:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1a9d5b99-8ec6-3ab0-8710-c4f38385fc83 | -6.41137 | -44.15782 | 2024-10-25 16:52:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 68059b8b-b052-305b-b392-eba9984baf44 | -6.3281 | -44.20107 | 2024-10-25 16:52:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 52cd3116-61ec-398a-a906-3fbc14eaaadc | -6.2719 | -44.10854 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2aa42070-ee75-3c57-bbb2-27408a2a3ef1 | -6.19782 | -44.20556 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7c134329-8002-3d00-91ea-e36e274d3512 | -6.19781 | -44.20768 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 9b68d5fe-cd40-39fb-b749-c618e06d833e | -6.19718 | -44.20388 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 0aa9fa80-ab96-323f-a2b5-a5965cacd2f0 | -6.19277 | -44.20445 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 5442cd8c-8cfe-3f44-a3ac-c2d3865e4917 | -6.19202 | -44.08909 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dde41a7e-02b6-3690-957b-a30d3e7647e4 | -6.19185 | -44.0913 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7ad6ed43-3cb0-3918-b1f2-904f091a8f41 | -6.16475 | -44.06134 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a63832a-8d57-300b-aa43-6e2bcc193326 | -6.14286 | -44.20259 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2dac929-7bd2-3450-8ebf-ef36fcb8adfa | -6.14114 | -44.02882 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aecb2b98-0602-37ec-a4b8-3072d2f7e84f | -6.06661 | -44.17851 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a05d6724-5d3a-32dd-9942-e5fcd6dae095 | -6.0615 | -44.17496 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c3cdf7c0-ba8f-309e-8cd7-db94f47b1764 | -6.04575 | -44.07966 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b99dac37-1156-3301-8e8b-f6931af64090 | -6.04505 | -44.07539 | 2024-10-25 16:52:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 291447b0-58e9-3ac1-aa0c-e56d93c0cd26 | -6.48299 | -44.3686 | 2024-10-25 16:52:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96033826-3390-3d55-bcb5-c4c784328836 | -6.47395 | -44.31497 | 2024-10-25 16:52:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 68a2a698-e265-3d26-b367-dfbd7434af89 | -6.46342 | -44.41015 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 829792a3-751a-39ab-a7bd-196825423da0 | -6.4567 | -44.67788 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9a986035-0d1c-3018-b274-d92ae34dd85d | -6.45246 | -44.67847 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 81f0fd30-6b95-3a8c-9561-b307dfdbd650 | -6.42894 | -44.87334 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| e272f8aa-0014-38a1-ad48-20ec3c161437 | -6.42829 | -44.86952 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| c3019bfd-c32c-31fb-ad88-efefdb156c4f | -6.41608 | -44.40602 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| cc2418f6-e2d5-34f5-8b7b-b357910422b6 | -6.40519 | -44.31339 | 2024-10-25 16:52:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 478bc34e-2c4b-3c97-95f1-b89a4f9854b1 | -6.39367 | -44.6629 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e6157bb4-05de-3216-a914-2e2835fdd1b6 | -6.39332 | -44.66317 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4036717f-c6a9-3dbf-b2a2-277a464fc057 | -6.38285 | -44.78287 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ed9a6abe-8273-331c-85de-dc535b0cce07 | -6.37317 | -44.67072 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| da9caac6-a915-393a-801d-326c606d8c3d | -6.35976 | -45.00586 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1bcee359-3b34-31b2-bc39-bc4d72f3e19c | -6.25741 | -44.78556 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 250a5e70-98d4-36e3-b598-59b43ec484d1 | -6.25527 | -44.64016 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 216.7 |
| afe6c693-eb13-3977-bb2a-a5adb6815141 | -6.25462 | -44.63619 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 216.7 |
| 2f6bde80-5ca9-31f6-8402-59a723efed56 | -6.25035 | -44.63683 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 216.7 |
| b804db45-657a-3a96-a618-72e1bf2bcdd9 | -6.22354 | -44.91853 | 2024-10-25 16:52:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 60eb3227-d7fe-3668-b717-08504ad8ab9c | -6.2187 | -44.91528 | 2024-10-25 16:52:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 09a9bddd-ac05-3698-b21c-3ad9b9e30392 | -6.21755 | -44.91537 | 2024-10-25 16:52:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cf355c79-a77b-3058-9a6f-856afe8d55d7 | -6.21601 | -44.84825 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a3281511-3eeb-3efb-80cd-2b47653decfe | -6.21557 | -44.76848 | 2024-10-25 16:52:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README171.md)
