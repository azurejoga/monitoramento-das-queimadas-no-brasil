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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c5d40fa-224d-3573-9f89-ebab88f0f8cf | -2.73701 | -45.2089 | 2024-11-11 03:55:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 5468b2cc-7792-3dd5-b164-38955bd260c8 | -5.27243 | -37.94533 | 2024-11-11 03:55:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| baeeb776-5bf4-396b-84fd-ba0cd117cfc4 | -2.19779 | -46.40645 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be8c929c-0fec-3c99-bdd4-a0fdc7ca542d | -1.98593 | -46.45206 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb7e3fc5-5263-3115-80f4-95668b6a5695 | -3.14036 | -45.97143 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eb440869-4a37-3211-bf99-f0c40a5e2ebe | -2.70045 | -49.34108 | 2024-11-11 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f95d056c-8a1f-3432-8fc6-4b5bc12abd88 | -3.54012 | -43.17225 | 2024-11-11 03:55:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25bddf86-1460-3eb2-ae06-a471e1c0e25a | -2.42172 | -46.52127 | 2024-11-11 03:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a76ddd93-12ee-3c5b-8ed3-ad41bf3eff81 | -3.595 | -44.55083 | 2024-11-11 03:55:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 475dded3-ad34-3802-a67c-b251bf01f726 | -1.65265 | -47.99018 | 2024-11-11 03:55:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bdc99af-2bad-37b3-8aed-5dc6a4283431 | -4.70027 | -46.42738 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba82badc-1124-366f-aac5-458a638cdd4d | -2.6991 | -46.66912 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02f149d3-c21a-3de0-af77-5ee73cc31ce5 | -2.44171 | -46.24106 | 2024-11-11 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ffcb0e30-42f8-359c-95bd-98f8a0eb1111 | -2.23046 | -48.38873 | 2024-11-11 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| d49ce4cd-388f-3a1e-a955-79aff11a0865 | -3.68932 | -45.24186 | 2024-11-11 03:55:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a028224-96aa-3134-b2e5-840b20e35ada | -2.1895 | -48.37783 | 2024-11-11 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| da9c6f23-409d-3e16-9d6c-b4491cd369d5 | -1.85096 | -46.5819 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a8f20e5d-14de-3be2-a2c0-b4563d4d53cf | -2.9994 | -46.93686 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b4f33e55-2956-335a-9837-54e6a58f50e1 | -3.23932 | -45.38198 | 2024-11-11 03:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ad38d149-6b61-3db1-9952-c82affdd720e | -2.24515 | -46.51356 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| caa5dfb0-f50e-3e01-b7b4-0b0ed88727f0 | -2.2499 | -46.51756 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 824508c8-96e4-3cf9-a8b6-b466b903038d | -2.23566 | -46.4398 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6da9b331-5d0b-382c-9f40-3133ecde1fc2 | -2.69888 | -46.67353 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e229700b-6864-3cfb-af42-f9a8bb283178 | -4.71181 | -46.39009 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10013d1b-4d2e-38ba-b85d-6d1d835e3e2a | -4.06851 | -43.95372 | 2024-11-11 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bddefc1-2c39-3cf9-9f24-fa8ec1f593e5 | -7.5997 | -34.9394 | 2024-11-11 03:55:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a3b3bcf9-d2c2-32d2-a2c9-fcd7fd3df9fe | -2.40231 | -50.31979 | 2024-11-11 03:55:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a06c139-9864-3b5f-a17a-56c7c0652b37 | -3.12427 | -45.97453 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8c94ad0-e430-3b85-8091-7bce73ac5af3 | -2.40708 | -46.77484 | 2024-11-11 03:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09eb251c-d005-3b98-954f-0af0230b2f62 | -2.41699 | -46.51728 | 2024-11-11 03:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12d8c35b-0779-3209-8c1c-433d1f2422e8 | -3.56052 | -44.95602 | 2024-11-11 03:55:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 241d1170-ef26-36d3-9fb7-ffed69599015 | -1.84701 | -46.58088 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 53e50415-d6f6-3177-a8ce-aca39ad22f11 | -2.19178 | -48.37992 | 2024-11-11 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f78e875a-2cb0-37cc-bc1f-fac2a95fe947 | -2.2634 | -48.75363 | 2024-11-11 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3559aea-32f4-3452-8f4b-581a75637390 | -4.69924 | -46.43339 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f4ecf7bd-bb32-3133-806e-116717e80411 | -2.40763 | -46.7715 | 2024-11-11 03:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cf1cf42e-f5cf-314d-86a9-32f15aa686fa | -2.69856 | -46.67233 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52052e7a-2c2f-30d7-97ff-ca5911461880 | -7.36937 | -35.08681 | 2024-11-11 03:55:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a5b9041f-85b3-3767-b5cc-155617fd614a | -3.27385 | -46.31918 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95708d75-5f0a-357d-a320-fde532c6f0c7 | -8.07358 | -34.97746 | 2024-11-11 03:55:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 17db01c3-2444-3e3b-b174-bbe301858b73 | -6.01112 | -38.66217 | 2024-11-11 03:55:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 33b3b2a1-d3e7-30d1-89dd-108d30c5f027 | -2.51726 | -47.34484 | 2024-11-11 03:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aae74b96-24e7-3fee-8781-e708948aafeb | -2.98901 | -46.99873 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 169b29ee-6bd0-3d23-9edd-f409c9bd6aa4 | -4.69976 | -46.43039 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79e22b43-7670-30b0-88b4-6ff51fee9d69 | -2.83786 | -46.64544 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 124a194e-0812-3562-81f2-458f15e7237c | -2.65555 | -49.39371 | 2024-11-11 03:55:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90651099-af4b-39ab-a5be-4e958a2f058b | -2.54365 | -47.32261 | 2024-11-11 03:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71273f82-8e09-3321-b7de-1c2d81f3d921 | -22.92156 | -45.41391 | 2024-11-11 03:59:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d113e58a-d4d4-3e96-a597-077685be9438 | -19.98135 | -44.10471 | 2024-11-11 03:59:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 4122c9c4-fa55-35c8-b39c-7366fad3edb2 | -17.6991 | -54.09029 | 2024-11-11 03:59:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 98b12b64-975b-3536-91ca-4e40a6a2c6e9 | -17.6987 | -54.09205 | 2024-11-11 03:59:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a7a69067-ad1b-3c34-aafb-d1c73973f2a8 | -19.8382 | -40.08194 | 2024-11-11 03:59:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 262d2ce1-df64-39f2-aed2-390a9a4adb51 | -17.69776 | -54.09613 | 2024-11-11 03:59:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c766371a-100c-3b67-b844-df0f55c218be | -18.6375 | -52.14335 | 2024-11-11 03:59:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0aa646f9-1f1b-3d19-a7ed-451d9b96dc9e | -18.32558 | -55.58241 | 2024-11-11 03:59:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a478361d-dc22-39b8-be5e-862dc6a9148c | -18.63656 | -52.14756 | 2024-11-11 03:59:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57372303-8534-37d5-b17d-528410af6d22 | -19.2746 | -39.89457 | 2024-11-11 03:59:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4bfad492-87cd-3030-80a5-ceb3580150fc | -19.30399 | -43.7142 | 2024-11-11 03:59:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 34a7c57b-3c01-3e6a-b0ad-7c46094d8262 | -19.98202 | -44.10069 | 2024-11-11 03:59:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| edd1e4fb-c42f-34de-8f46-d16b1b97a402 | -20.76395 | -46.77139 | 2024-11-11 03:59:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 036e06f0-a258-31e5-98bc-a7eee2fbfb7d | -2.2297 | -53.6824 | 2024-11-11 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| b8b8a6ad-5896-33ee-8e39-8a27d9a88b1b | -2.2445 | -48.3802 | 2024-11-11 04:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a8aac3fc-153a-3f76-80e5-24af40268974 | -3.1458 | -54.4859 | 2024-11-11 04:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 86cebb83-c494-3140-8084-0a3dcaac8704 | -2.7402 | -49.3502 | 2024-11-11 04:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 0dd31706-f7ff-37aa-a26c-adfa2ddc6a50 | -3.2588 | -53.6994 | 2024-11-11 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 13fa6c9f-a783-3332-914e-aae92b244094 | -2.8672 | -45.3507 | 2024-11-11 04:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 683672f2-0277-353e-ab29-fd0d90cc99c3 | -4.7023 | -46.3842 | 2024-11-11 04:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ca5a2e8d-7d2f-3049-8501-e0acecab9640 | -2.2663 | -53.7422 | 2024-11-11 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e785771a-1c80-37fb-a535-e1ca69a3f5e0 | -2.2075 | -48.3811 | 2024-11-11 04:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 05522193-d2b4-376d-a4c3-06c19902dbd7 | -2.7378 | -45.1976 | 2024-11-11 04:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ef34e0ff-a247-3974-bb00-31046de01541 | -2.8671 | -45.3732 | 2024-11-11 04:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 135.6 |
| c9e0b0e6-8fd6-3098-ae15-ed7dcc4b1290 | -2.248 | -53.7426 | 2024-11-11 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| c70c19e4-2d96-3a2d-acb4-f679e7140b96 | -17.2933 | -57.4857 | 2024-11-11 04:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.6 |
| b233c69e-fcdc-3cd9-bf4d-c03ed574407e | -4.7209 | -46.3832 | 2024-11-11 04:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 1ebc29fc-81bb-35cd-90a2-dc0b44bd66a7 | -2.1891 | -48.36 | 2024-11-11 04:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| b3c36c85-5208-31b2-9319-a39432c2fa59 | -17.2936 | -57.4652 | 2024-11-11 04:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 0df2dd4f-061a-3511-9982-00225f78c108 | -2.8857 | -45.3726 | 2024-11-11 04:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 111.5 |
| f0f0134a-bcf5-3ae1-95cf-0475e6a34edb | -2.2259 | -48.4021 | 2024-11-11 04:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 77d9f848-971a-37e6-a466-a6d9a021be5d | -2.189 | -48.3815 | 2024-11-11 04:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| bbd7cbff-08a2-3c69-b9e4-14c7b5ddf372 | -2.7587 | -49.3497 | 2024-11-11 04:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| c8c182d1-c0bb-35d0-8bd1-b8802daf65a5 | -2.226 | -48.3806 | 2024-11-11 04:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 882af6c3-f079-3082-8bec-c2b51f37e593 | -2.2298 | -53.6623 | 2024-11-11 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| c52a819c-fb34-3b6d-a970-8355e3c81746 | -23.9283 | -54.04779 | 2024-11-11 04:01:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 38c00d19-e00f-3cb9-b0be-3b1e3eb6a055 | -23.52159 | -46.97511 | 2024-11-11 04:01:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5888993c-4485-39d8-8dc0-e81888c0a407 | -23.91799 | -54.04039 | 2024-11-11 04:01:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 43ecc2f3-0d1b-3f57-bcca-96e8b38b6bab | -23.34092 | -46.77132 | 2024-11-11 04:01:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b04975d4-76e0-303c-a6b9-f414e005ba7c | -28.58925 | -49.44362 | 2024-11-11 04:01:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2671ef00-b690-31f6-8d42-44fa57ccf181 | -23.33996 | -46.77393 | 2024-11-11 04:01:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8f351598-343b-3c30-b419-fd48cb60d617 | -28.63356 | -51.30371 | 2024-11-11 04:01:00 | NOAA-21 | IPÊ | RIO GRANDE DO SUL | Brasil | 4310439 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 34a40a78-6b60-327d-a6d0-c5fdf9e59f89 | -23.92932 | -54.04349 | 2024-11-11 04:01:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| c701b828-393f-3cf9-9d4b-cc5486bd30d6 | -23.91672 | -54.04153 | 2024-11-11 04:01:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 560a96ef-ebcc-3db5-86fd-8a1b52784213 | -23.91771 | -54.03724 | 2024-11-11 04:01:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7972b329-9ef1-396a-a9c2-ecf56fde74f5 | -23.92366 | -54.04194 | 2024-11-11 04:01:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 6147806a-f310-356a-a7a4-5c8153be155e | -24.63195 | -52.88387 | 2024-11-11 04:01:00 | NOAA-21 | CAMPINA DA LAGOA | PARANÁ | Brasil | 4103909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 74653e5a-51ad-3d91-b9f4-a3fb601fcdb8 | -23.59554 | -47.43771 | 2024-11-11 04:01:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 48a84b1b-fc4c-3d8a-8cf8-5c62234beb52 | -29.87458 | -51.15746 | 2024-11-11 04:04:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| c22682d4-502b-3403-be97-79981438bb59 | -4.702 | -46.4286 | 2024-11-11 04:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 70f6bb4b-ca52-3640-91bd-157f2f11d1bc | -2.2259 | -48.4021 | 2024-11-11 04:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| fef1838c-04dd-3382-b9b1-adf17bb5a206 | -2.2663 | -53.7422 | 2024-11-11 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| d7427e28-fdf1-390e-ba2c-48517d52c25e | -4.7209 | -46.3832 | 2024-11-11 04:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |


[Clique aqui para ver as próximas entradas](README27.md)
