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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1111e34-0447-3679-9c0e-fcce54124044 | -9.6122 | -64.04842 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bab30750-acf2-3914-b71a-5eb41d132c8f | -9.61151 | -64.05246 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3642e1df-851e-3e57-a3f7-0d3c36e7fb1e | -9.61093 | -64.05159 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6fa47c5-1b0d-32b9-83f0-eec233b6e04a | -9.58308 | -64.2318 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac8a316e-d538-3ae1-bf3a-e0db23ff5233 | -9.58141 | -64.22823 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8d9a911-235f-398f-b34b-f8f58f7fe3d1 | -9.57952 | -64.22689 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b47d113f-97ca-3a18-99f5-85fa6d0b9f10 | -9.57782 | -64.22333 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b6e9f50-781d-36a1-b77a-f22a4178ec2c | -9.57711 | -64.22743 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44959428-e845-3579-8401-ae8070454509 | -9.57423 | -64.21841 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e3d84b5-ce76-38e7-af15-55ff0124b6dd | -9.57352 | -64.22253 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4563db6b-8f83-36b1-80f7-6ce911317f78 | -9.57282 | -64.22662 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e3e20d7-fb07-354c-9d5a-ede787ab4486 | -9.56993 | -64.21762 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7787a6d6-c938-3180-88e4-dc7757f5894b | -9.56852 | -64.22584 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0725f9e5-295c-39cd-b4b9-595ee47d5e8b | -9.42256 | -63.65965 | 2024-10-06 05:12:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| baad113c-74d2-33b6-95a2-55925456f156 | -9.42143 | -63.69108 | 2024-10-06 05:12:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bfddf5a-db7a-3ebb-8a4a-10d0226ce642 | -9.37923 | -63.71159 | 2024-10-06 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa439bee-b189-3d5b-afb5-4ca097d37639 | -10.5921 | -64.41472 | 2024-10-06 05:12:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a134c5f-ad71-388c-801a-10f0320fa262 | -10.26205 | -63.32909 | 2024-10-06 05:12:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1af5bc05-71c2-3b30-9deb-689b187525fb | -11.00338 | -63.57549 | 2024-10-06 05:12:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 475523f8-9681-37b4-8c50-01c218611689 | -11.00248 | -63.57515 | 2024-10-06 05:12:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22d444ac-3629-348a-8b09-f1d7a0c40422 | -10.99934 | -63.90659 | 2024-10-06 05:12:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 701fcc2d-d9fc-34d1-9ebb-1227a6c3d8bf | -10.99866 | -63.91043 | 2024-10-06 05:12:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8bf25bed-ec48-3727-8754-c7671b263ad3 | -10.99799 | -63.91423 | 2024-10-06 05:12:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c850975f-e69b-397f-a09b-7c95e34e849e | -10.99518 | -63.90611 | 2024-10-06 05:12:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fcf75c19-3de3-32d1-80ea-a6ab61442971 | -10.99452 | -63.90987 | 2024-10-06 05:12:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ceaccfc7-bc68-3d5e-8350-36f981f9dd65 | -10.99385 | -63.91368 | 2024-10-06 05:12:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d71d632e-5e87-3c7c-a302-e13eaa5bf527 | -10.99251 | -63.92131 | 2024-10-06 05:12:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 041b65d2-9593-3eb1-b6bf-e67e17d6c6a0 | -10.97831 | -63.97771 | 2024-10-06 05:12:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 02bcdd55-ed74-3ee3-ac23-2dc2f3c553a0 | -10.91916 | -63.88848 | 2024-10-06 05:12:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96065f1c-7027-3c07-8e48-6f3cdf3dbf0b | -10.91514 | -63.88723 | 2024-10-06 05:12:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3b6cbcc-8ab3-3600-94c1-9008d93ae1da | -10.8983 | -63.91076 | 2024-10-06 05:12:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6dcababb-18c7-324f-addb-6442a6e37455 | -10.88602 | -63.90809 | 2024-10-06 05:12:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| baa30bcd-9015-3e6b-9133-cea2fc0ebd34 | -10.88253 | -63.90379 | 2024-10-06 05:12:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2aeb645f-f3d5-3d2a-a2f7-2df26033923f | -7.51257 | -64.67889 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d065685-9394-31b9-9782-844d1ecd2f61 | -7.37743 | -64.66803 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a75e2593-009e-3515-accc-02ea16a76af0 | -7.37367 | -64.66247 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d82f5d50-d3f9-34fa-aaa6-e0e17a3c3661 | -7.37283 | -64.66723 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be7a30a5-709e-3122-91ef-56ffdab77f7a | -7.372 | -64.672 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 61cca3a2-b43f-32a5-87d2-b399689ac398 | -7.35482 | -64.68882 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 817bf8d0-afe0-311c-9606-b12a5da9a8e6 | -7.33018 | -64.67075 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48ec9cb0-89e1-36c9-9f6b-77459738c830 | -7.32972 | -64.66972 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a3d5d07-7059-3c3b-bdab-9f263d9bccc1 | -6.81888 | -64.32233 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df3a4477-cfd2-3635-9e59-bed016dff731 | -9.368 | -64.31683 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| facbbb35-e6dc-3cbe-8f35-3995d1af6dcd | -9.36724 | -64.32107 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a248b652-008a-31be-81b5-4b4dcf986450 | -9.36649 | -64.32529 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4a66ad90-9110-3a10-a070-217ce276a655 | -9.36574 | -64.32951 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1dfacf90-8c84-32d7-ba85-6fb1f166c81b | -9.3629 | -64.3203 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8de791b1-da4d-30e4-8a7a-ccb19812241d | -9.30982 | -65.38059 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0b4b136-b425-3730-9c7d-2a807d70965a | -9.30604 | -65.37479 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f8fe0e6-0924-3b2d-a571-e5bf7c14316c | -9.28763 | -65.42333 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d936ff12-8a6c-3b1b-b37b-1458ed7809da | -9.2712 | -65.36609 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 715b4902-4e12-3a57-b3e4-26d6c83fa64a | -9.26962 | -65.36302 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5eaa0091-a699-3385-bbae-94de2d036a0e | -9.24932 | -64.32235 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22e3f045-2f13-3ba4-a7ba-e18d8f7a385c | -9.24018 | -65.60414 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f3c1e16-a0ef-3f2a-a738-e4f709a7b241 | -9.23886 | -65.607 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9df1f70a-b6d8-34c2-b1dd-6a1787e19bde | -9.37084 | -64.32605 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac42e01c-5bdb-3453-8ae5-bb26920f44ee | -9.37008 | -64.33028 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbee7206-dcb2-39f9-b9fe-0ac9d5576d4b | -9.36934 | -64.33451 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd7d5b69-61e1-3b77-a9f0-c100698cceb8 | -18.73243 | -57.33433 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 78018ef6-e3e7-37d0-8017-6d61629b6682 | -18.72177 | -57.35836 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| d319f51a-6623-3349-a3d8-204240c6e58f | -18.72117 | -57.36255 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 973947dc-aabe-38b3-9d6a-8114ceaa8a7f | -17.84384 | -57.69188 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 59d06f1e-8e55-37c8-bb59-f98a6fec0289 | -18.64506 | -57.28808 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2ca03334-02d2-35b5-8c28-8c47adb91a07 | -18.64446 | -57.29228 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 604fa968-dd25-3b46-a6a6-908784da409e | -18.64392 | -57.27069 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 3f79f351-78d4-3dd7-964c-28f6d9f5a7ff | -18.64332 | -57.2749 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 700f6299-8446-3932-83d7-31bfeb90838f | -17.84787 | -57.68845 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f3abbb0e-b3a9-3ebe-bfd1-146a3a36acc4 | -17.85247 | -57.68104 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d9b88caa-cd31-3ad5-a38f-2c3d356d47ce | -17.8473 | -57.69243 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f75ab7b8-54da-311d-b362-db658a0ec8a5 | -17.83924 | -57.68427 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| a918d2c2-1501-3b85-8fe7-b806f9b71313 | -16.973 | -47.12265 | 2024-10-06 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6bc768c-4579-308b-9e44-dce23dbcda91 | -16.96049 | -47.12182 | 2024-10-06 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef1d52b7-3175-3eb7-ba6d-1674396f874d | -16.95993 | -47.12107 | 2024-10-06 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b73aae4-4666-3332-8e2e-ae451e55f319 | -16.95399 | -47.12067 | 2024-10-06 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 777a727f-3587-3332-8ecc-40e13cbc5332 | -16.95345 | -47.12615 | 2024-10-06 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9887d15f-d847-3af4-b2e2-75a62dbca196 | -11.54221 | -65.13828 | 2024-10-06 05:14:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28d4ed94-14a7-336a-9fed-d086c393ab4d | -11.53455 | -65.05491 | 2024-10-06 05:14:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e9ec8da-8924-3a81-963f-72e1c4305b37 | -11.53095 | -65.04974 | 2024-10-06 05:14:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1cae20e5-1c6f-3fbf-9ae2-f4d92baaaaac | -11.53015 | -65.05412 | 2024-10-06 05:14:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9dc74c44-d374-3e05-a23e-c849c68f5f0e | -11.52935 | -65.0585 | 2024-10-06 05:14:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1877e201-4b9b-35a3-9abe-b3a4b103c769 | -11.52575 | -65.05333 | 2024-10-06 05:14:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 63795450-d4fb-3175-81db-b90108495279 | -10.62664 | -69.63185 | 2024-10-06 05:14:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 937a68d4-d159-33b1-8761-d6468ca284c9 | -19.6589 | -56.46093 | 2024-10-06 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c7a10732-0c11-303d-9e90-4ffbb75fdf64 | -19.65827 | -56.46568 | 2024-10-06 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d2f0d82a-a974-3aca-8c1a-10b7fbd06556 | -19.65764 | -56.47042 | 2024-10-06 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cbd78501-b362-370a-8af1-6acfa0f57380 | -19.64331 | -56.49236 | 2024-10-06 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 672f723b-3622-3b4f-bb63-ad187df69bb6 | -19.63958 | -56.49179 | 2024-10-06 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f9ae5ec8-7f86-3c3f-83c4-2aa8e9f16480 | -19.58723 | -56.52933 | 2024-10-06 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 02460145-6699-3556-b2a8-37c273ba3d79 | -19.58351 | -56.52875 | 2024-10-06 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 54728deb-d9e3-3057-934f-bd991ad4fa05 | -18.71823 | -57.3578 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4d4f2acb-7516-30ff-b4fd-f047790a9272 | -18.71763 | -57.36198 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 163fc483-0b4c-3d3e-96b3-9c02be8f2e71 | -18.7141 | -57.36143 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 3c0fecd0-a9ab-3b4a-ab70-eb05b6b1396f | -18.7135 | -57.36562 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 89a8070a-095b-3f9f-a022-69acc1df5117 | -18.70765 | -57.27881 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5f161c17-fc4b-323f-82a7-413cdb0505f5 | -18.70646 | -57.28725 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 135251db-cbd1-3530-81e9-9b21d235dc8b | -18.70528 | -57.29567 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 9b0a5f52-a0e6-33e5-86bb-6f20926306da | -18.70469 | -57.27404 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2f59323a-9b61-342d-af2e-451164454ab0 | -18.7041 | -57.27826 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 20fd364c-38d0-341b-8a65-c75063f23f4f | -18.7035 | -57.28247 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a9b6959c-daca-342f-ae18-7afab6ab4f7c | -18.64037 | -57.27013 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |


[Clique aqui para ver as próximas entradas](README113.md)
