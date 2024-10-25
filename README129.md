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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e91d32c0-b65d-3b97-8dc1-8fef3e827fac | -19.61824 | -56.68239 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 065d2d73-b8ae-38d3-a4df-86a3ba8ec021 | -19.61789 | -56.67904 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| f1c12613-64ac-3043-9f7d-4c9bb93e0902 | -19.61754 | -56.67569 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.0 |
| cdbe692e-ab9f-3b34-88e8-98c09f09f4e1 | -19.61685 | -56.66899 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 27.3 |
| 13d6233e-ea26-3a27-9fe1-f9994dd19471 | -19.61334 | -56.68631 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| e087020e-1d7b-33e3-83cf-a0fd12ec60ec | -19.613 | -56.68296 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 6c5ebfaf-55b1-3b44-85ac-9b5dd8fa4dc7 | -19.61265 | -56.6796 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 778e9b87-9e82-3d24-b28e-e4ee4f775a9a | -19.6123 | -56.67626 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 7bb9c5be-a118-327e-96ee-752396c5df8d | -19.60775 | -56.68353 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| bbea070d-197b-3be3-9328-cf8b6e3585d4 | -19.60741 | -56.68017 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 9ccff804-c4b9-3b1b-be5b-474c5c3935f4 | -19.60706 | -56.67682 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 7b84db4d-ddd3-3d85-ba47-313fef6d0803 | -19.60251 | -56.68409 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| ce267ba1-e98f-3992-a885-dbeb4e743b2c | -19.59735 | -56.63398 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 19033fca-a576-3817-a8a4-e2bce6648f0b | -19.59701 | -56.63065 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 3a9f6408-9476-35f2-83f4-f6e1570dd593 | -19.59247 | -56.63787 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 886b559d-b0bc-30e9-ae59-8552be3c478f | -19.59076 | -56.62127 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| f131cb4d-68aa-3f7b-9a78-65663fcea016 | -19.5836 | -56.65915 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 8338275e-a909-3bea-8578-72a740f76bc6 | -19.58288 | -56.65251 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b8e5b9d0-a29b-318c-9208-ec7f805413a7 | -19.58251 | -56.64919 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8a222edb-b2ae-3806-ae7f-37eec3ae1df7 | -19.57308 | -56.6031 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| d4eca38d-b073-373a-a09b-c74fbfec3a96 | -19.56786 | -56.60367 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| ac4247b5-2224-3f50-98fc-a107d18d0923 | -19.53339 | -56.68481 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 0affbd69-63c3-3fb7-87b4-57533bfedcda | -19.53304 | -56.68148 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 9ff4c443-9163-3bba-b41e-7624aef26e12 | -19.52815 | -56.68539 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| a8cdc82a-ebef-3dc7-89bb-c54b71cd04dc | -19.51384 | -56.59958 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 15e3cacc-4471-3ffb-ad7c-0eac42ca5457 | -19.51349 | -56.59629 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 0a13159d-6bce-3842-b675-93e4baf08a37 | -19.5128 | -56.58969 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| d59c4a64-e399-3cf7-af52-ccdeb294ff7b | -19.50092 | -56.67818 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| e79d1a77-fb07-3bfe-ae57-1d9d7a5dbb6c | -19.49644 | -56.63493 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 0b9cb1bc-3f25-3c31-8bcc-6af1bb935053 | -19.4961 | -56.63161 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 85d8e97c-748b-3425-a578-35b0bb6e06f4 | -19.49534 | -56.6754 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| c7df3183-ac59-3f05-a445-0199b05c05cc | -19.49499 | -56.67205 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| dcf25f3a-94bc-3d04-8ae9-5d01e718f083 | -19.49465 | -56.66872 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.1 |
| 4db1bc92-c214-3913-a3bb-b6d4f2c07fd0 | -19.49088 | -56.63218 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| a31f73e2-ea73-3ce5-9add-77084f4c956b | -20.65332 | -56.24637 | 2024-10-25 16:48:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2891dec-dd84-3ec0-b555-69631d34595f | -19.66111 | -56.99386 | 2024-10-25 16:48:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 66cc5194-2b50-39fe-93ce-b60e66b080bc | -19.6195 | -56.99088 | 2024-10-25 16:48:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 0b9e9cdc-ac1b-3692-a3be-c4866b6fbb62 | -19.68069 | -56.97404 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 1b4b2b84-6ae0-3295-a55b-d961d89d494e | -19.67571 | -56.97812 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 24.9 |
| 5de917c1-3f6a-368b-bc30-f311bf286b8f | -19.67535 | -56.97461 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| ffd61445-8d19-3808-9103-b7e27bd3e9ef | -19.65966 | -56.97982 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 25.9 |
| 1cd53ebb-24d7-32d0-be55-787924146f5f | -19.6593 | -56.97631 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 45.2 |
| e9272cbd-a367-3b89-921b-67bd01e1dbb9 | -19.65384 | -56.87125 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| c0e91a22-9b04-3e9d-ab1f-62dba408b9eb | -19.64853 | -56.87183 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 4ebc4229-552d-3272-a55b-23e5242a1942 | -19.64817 | -56.86837 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 9d38fd31-9ca7-341b-9d9c-a16b23ae7c66 | -19.64552 | -56.68965 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 30.8 |
| 7fd479e3-cc48-358d-8b2a-07a38ee1dbc2 | -19.64322 | -56.8724 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| a6b2a248-d138-395c-a410-a7d9786fca7f | -19.64287 | -56.86894 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| e703cc42-eb94-34fe-b37a-408953b1cf9b | -19.6424 | -56.71037 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 5dbe1fa3-9983-3f19-9c7f-d0f97554bc39 | -19.6382 | -56.72105 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 8638f70e-a4a3-3029-92c7-b9bb8545df7e | -19.63791 | -56.87296 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 3385a52f-a1f9-3194-a7b5-ff2abb0aa74a | -19.63785 | -56.71768 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 20367314-cbe9-3ea7-933d-e75adb98076e | -19.63756 | -56.86951 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 9c968ecb-23af-391b-8e78-ce40d4f17322 | -19.63749 | -56.71431 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 3664d4cc-b5e9-3fb8-a553-216cec73c9a6 | -19.63714 | -56.71094 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 931398c6-dc2a-3a32-a3cf-ed545b6d9bfc | -19.63189 | -56.86662 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 2bab8e4f-61a4-340e-9cd5-807edb741e1b | -19.63119 | -56.85972 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 8a5f519c-e7ed-3782-ac49-43ff2e12c34d | -19.62943 | -56.68797 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 554d2061-3713-3bef-917f-7736f8ddbb31 | -19.62908 | -56.73568 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 5cd2b577-77e9-3ac6-9f98-5c6f56716e68 | -19.62623 | -56.86374 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| a9ddad68-ef43-3262-a9a4-a06756081c91 | -19.62588 | -56.86029 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 72e0bd67-a958-3559-ae10-e1c385faf1d2 | -19.62452 | -56.74301 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 73e128f0-6f1f-3c67-b8c6-abde72d77058 | -19.62418 | -56.68853 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| ced3db17-e402-3cc9-a86e-c6ef7ec12c52 | -19.62417 | -56.73963 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 4fb62d71-ffb1-355f-8218-93b89d575813 | -19.62382 | -56.73624 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 5d5cd04c-8239-3c99-bfba-6bbe7340a810 | -19.62293 | -56.9908 | 2024-10-25 16:48:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 2cb3bc48-c232-3cce-b140-fd11cb0ca1e8 | -19.61995 | -56.75035 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 32.9 |
| de655bc6-dc95-3e77-9e41-6d8b23947b97 | -19.61894 | -56.6891 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| ccd94ce0-f81d-3016-96c5-8718f43c9ed1 | -19.6145 | -56.90694 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.8 |
| a127c0cc-8e2c-384c-bc8f-389d44fc8ded | -19.61415 | -56.90347 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 42f64dab-84df-3d5e-8f64-d960c89b4920 | -19.61404 | -56.69302 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 5179e17c-0573-3bfd-9c45-2648b989d1d2 | -19.61369 | -56.68967 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| a3201cf1-425f-371d-bafc-5e3945ad0670 | -19.61087 | -56.91066 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 1f0f3795-c27e-3869-b48d-8e6244b9ffbf | -19.6105 | -56.90719 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 52126e04-75d9-38b3-90ba-34def027d4e0 | -19.61012 | -56.90372 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| e9987b76-f0aa-3875-911b-e96c11d3e1a4 | -19.60953 | -56.91099 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 6b0f996a-29c1-3882-9d9b-66ff0f4b9fde | -19.60883 | -56.90404 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| b95455ad-929b-3d46-a169-f6ea24853524 | -19.60879 | -56.69359 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 5939318b-f0fa-30aa-a556-4cc05106c83b | -19.60844 | -56.69023 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.6 |
| 735d8a37-226b-3b62-a57c-e4070e1341b4 | -19.60354 | -56.69416 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 2e2f447a-f3b5-35f3-8e8d-eba4b49c2367 | -19.6032 | -56.6908 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.6 |
| 1e309f26-2efb-3480-9ed3-58bf057c8146 | -19.59339 | -56.69864 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 05e837a2-4ceb-31fc-9651-f593daa3809f | -19.59304 | -56.69528 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 9f1277f3-6336-30e6-b4f0-54c0a187aff4 | -19.5927 | -56.69192 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 0929a6cb-30af-3517-8535-7a21b040ee07 | -19.58848 | -56.70256 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 29.6 |
| a47a47a5-1e41-34ca-b5d7-968fb3281d9b | -19.58834 | -56.70265 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 32.5 |
| f2a05615-460b-3ca0-bd34-27f559d06330 | -19.58814 | -56.69921 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 320258d3-fdc0-305b-b16b-ab6b928a5064 | -19.58798 | -56.69931 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 3670b845-d257-3e83-af8b-6363f1af1b21 | -19.5878 | -56.69586 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| beaeb279-06f8-33b4-a447-0abd77f35392 | -19.58761 | -56.69596 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.5 |
| f2824d30-dcdb-3ebe-ae26-4c4f271ffe18 | -19.58289 | -56.69978 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 6bde1bfb-d958-31ff-8d39-077559c57a9c | -19.58273 | -56.69985 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 223a80bf-6488-3f78-8059-f367ed11d878 | -19.58255 | -56.69642 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| efa19920-b9ed-38f7-ac7e-24a37fc88ee1 | -19.58237 | -56.6965 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.5 |
| a56c5630-2c73-34be-82cd-54ae857b30a4 | -19.57764 | -56.70034 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 1a06be56-417a-34bf-80f5-2cd0b4d14a82 | -19.57748 | -56.7004 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 0eb57800-1170-3bec-9d34-0878806c6dea | -19.5773 | -56.69699 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 6232216d-d398-30d1-aa7f-b63ca61ef12a | -19.57712 | -56.69706 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| b148ae44-1ab2-3201-b72b-ac9687b5c25e | -19.54636 | -56.70713 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 2b294084-5f1f-30b7-ab52-4e03d674f552 | -19.546 | -56.70377 | 2024-10-25 16:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |


[Clique aqui para ver as próximas entradas](README130.md)
