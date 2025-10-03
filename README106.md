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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 055230e5-6cd4-36c5-a53e-0fc066edb886 | -10.04426 | -52.10199 | 2025-10-03 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 283657a3-6af7-3942-940c-1adc6d684280 | -8.33226 | -46.22323 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d66b128-b1ab-35dc-a70c-6063526166c8 | -5.78024 | -45.76491 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88cdfe06-879e-31de-8297-6e9958bea39f | -5.54197 | -44.6475 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 141680c4-b544-3381-bfdf-b0f0368343d1 | -7.01421 | -42.31481 | 2025-10-03 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1908fdd6-6f58-3ae9-b77d-705d50a0afbd | -10.63673 | -56.76677 | 2025-10-03 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48d1c1e3-999a-3d5a-b539-7237cc8acd94 | -10.86337 | -45.41336 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60a28046-cfa1-3f2a-8b3c-0bad8238077e | -11.01538 | -46.55072 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 15414c91-ebe6-3bb2-b542-bf1653ec14c0 | -6.32954 | -43.89039 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 721f57f4-2d7e-3164-9054-30ff8433d230 | -6.18005 | -46.28029 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20f968ff-d4f3-3605-b4c6-1e7a3f32136a | -7.74377 | -46.24924 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c44142dd-2137-3dda-a1fa-b07c3ec176ee | -6.709 | -42.80263 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 861e698b-366a-3a69-a3f5-2dafc0ce3784 | -5.78422 | -45.76174 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a72d8daa-6f74-3a99-8b9a-9a5fe18c7031 | -9.88259 | -47.81388 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 406df428-7fa6-3f04-a4ab-6fcbca6cc91d | -12.0624 | -44.86798 | 2025-10-03 04:32:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 752fe2ed-40ee-3d82-a1b7-1ccffe6e7e1a | -9.93929 | -43.75623 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ed69ea2b-3fe2-32da-8da7-8dc16d5277d4 | -6.0666 | -44.61679 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8e00e5d9-201d-3d6f-86f9-1710bef84e89 | -11.55937 | -47.65258 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d622a07-b103-3afd-997c-95e57aff820d | -4.25794 | -48.56079 | 2025-10-03 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbd387b1-189d-3200-bc31-cd70c9a90d3d | -7.71165 | -46.20651 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c7d1ce2a-870d-3432-985d-688c24fdeba1 | -5.34314 | -43.76383 | 2025-10-03 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c1fce6a1-1d20-34f1-948b-31f19411a236 | -10.89376 | -46.70858 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc6d3078-9878-30c5-bfd6-ba2b337e4a66 | -7.24728 | -49.40902 | 2025-10-03 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60774bfe-04f7-32c4-8815-6bac68b7579b | -6.66172 | -42.78844 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5bcd61e0-ec0f-3941-8db5-60efd2f05cbb | -9.40704 | -47.52945 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93001a30-0231-393e-8f5c-6a78e322acba | -6.70234 | -42.81976 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 728a9274-6361-3c2b-81c5-9c31a1e832e8 | -5.18169 | -45.42137 | 2025-10-03 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 206f29e9-b388-37c8-9d03-68dbc2cccee7 | -11.09734 | -47.83458 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db546d52-4173-37b3-8d35-3e0133fedab2 | -8.81349 | -46.67007 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3ce095e-c123-3b9f-9a09-a4517c9c7618 | -11.56834 | -47.66141 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d4f53ef-c7e4-35bc-9eda-c313f60144ba | -11.90818 | -46.30672 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdf78665-f137-3b18-bec5-699810fcc48c | -4.48342 | -47.67794 | 2025-10-03 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2dff5f19-1746-37b0-b741-527702fecc05 | -4.62234 | -49.37249 | 2025-10-03 04:32:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1e8839d-deae-375e-b6d6-ceff3cc08fcc | -10.9699 | -51.08469 | 2025-10-03 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ddb8bef-f00e-34f5-93e7-00a0d54ca92d | -4.64993 | -47.54902 | 2025-10-03 04:32:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ba6f279-ddb5-3772-af67-f1fe68b5b0c9 | -11.90403 | -46.31037 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef45f931-3d85-31d0-bbab-d2732c70c900 | -7.79063 | -47.38073 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a25e813-f0ba-3bfa-a4e1-8c471be4723a | -5.50056 | -44.91871 | 2025-10-03 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dc15dbe-ae44-302e-b7ff-0d45bfc518ca | -6.03966 | -44.62514 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c9b66c0-06e7-3ba4-b4df-b30bcf0ea8d1 | -8.45052 | -41.89856 | 2025-10-03 04:32:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 77e72e21-bf3a-3ff7-96d1-4b0eccf9f783 | -10.87656 | -47.05404 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b942b95-bd8e-30a8-82f4-29d3c537ed1f | -6.03699 | -44.63023 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f6b0a08-bd45-387a-99a8-fb21fe3e9fc2 | -5.35769 | -45.959 | 2025-10-03 04:32:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b5fc735-792d-3510-b482-76ad971f2be2 | -7.79172 | -47.37372 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 43374780-c3d2-3274-aeb9-34abeb6cba3d | -7.90599 | -43.53457 | 2025-10-03 04:32:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec01e84f-7231-3c96-854b-f5ab94e0553d | -5.78478 | -45.75803 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e603f0a3-cc9f-3b09-b2e8-89ab4d54b186 | -7.24949 | -49.41679 | 2025-10-03 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c7379d2-22ec-3359-a2bf-49e96b61623c | -4.95181 | -45.77507 | 2025-10-03 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7f0bdbc-f6b4-3cdd-951a-c4e9baeeb1d3 | -9.65758 | -48.20941 | 2025-10-03 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61333496-e385-3f16-b1be-20fd0bab245c | -4.67295 | -45.79263 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b54f5351-4453-36b9-aae2-0c48f1469bd5 | -7.86742 | -47.30305 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de8e0bea-46c3-3428-abfe-41db8f36b7ea | -4.48066 | -47.67397 | 2025-10-03 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 330fb544-f2ef-34e9-8d2f-864209ad8f8c | -6.03844 | -44.63329 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5924bcfc-0c08-3030-8871-0a71c9df1ad0 | -9.63037 | -54.31606 | 2025-10-03 04:32:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6faaaee-b82c-39bc-8697-120b958c2afc | -7.77324 | -42.50566 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fb06a0c6-c35d-3464-8e7d-f6e77d77379d | -7.29774 | -44.18631 | 2025-10-03 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec3a8f62-ad7e-33ee-85a8-f1e4c4ec0b2a | -5.17768 | -45.42456 | 2025-10-03 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42d28139-8d3e-330b-90e4-d4460fe99d59 | -10.61078 | -48.71302 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16e1c38b-fce0-3e98-8e3f-387e71b6a59b | -11.08744 | -47.70463 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cd9015b-f563-35fd-b714-8b0c8b025ebe | -6.37397 | -43.88113 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13493c14-07b0-38dd-a667-4d9c8febd91b | -6.59623 | -44.32473 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b60abcd-b6db-3117-95ad-61500008b7f3 | -9.44991 | -47.58324 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eb54218e-4b1b-3dba-b682-6eaff633ee93 | -10.87871 | -47.82199 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9c2e438-3788-3822-8db5-ba25b624a0ec | -7.00398 | -47.17891 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec7c9f2b-2045-3dad-96dd-c7b665eb3ffc | -12.22122 | -43.76992 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e30f767-9b9f-3486-bdbd-629ca96bcab9 | -10.11994 | -52.34538 | 2025-10-03 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f976a90a-c078-3df5-b853-3cb69677d5a8 | -11.09575 | -47.86709 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6a57b2d0-6b77-38c8-a49e-c71aeb7adc32 | -6.34447 | -44.30869 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58c43687-20d9-36dc-abd2-f096d9a03aa9 | -10.88975 | -46.71183 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47e81263-4b38-361c-87f5-4bf3b2b3c7dd | -9.06182 | -46.64763 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1a7e4ccd-4ab7-395f-b195-a871af0528bd | -6.37329 | -43.88571 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b192eb1f-427b-36ec-9d56-cf0c52b7872c | -9.8021 | -45.91945 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb501668-ac89-3c9b-9973-59b858ccfd05 | -11.212 | -41.59613 | 2025-10-03 04:32:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b89b016f-46d9-3f3a-b764-c3de0bb72ec3 | -6.68534 | -43.71029 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42de7c6e-381b-3074-887e-4547af93fdf2 | -4.65378 | -47.54609 | 2025-10-03 04:32:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ede85d8-b0be-3cc9-ad25-a6e3f338b6af | -4.57639 | -46.50382 | 2025-10-03 04:32:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b595655-ca1d-35a1-a30a-0a704bbb8713 | -6.24029 | -45.34913 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6b6090a-f144-314c-87f5-b29701be8a4c | -9.88592 | -47.8144 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cabffc47-d92b-3c0d-bc20-0215876e6b54 | -11.81182 | -44.89707 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e249cff1-04c2-33a8-8d82-f3883e3eea79 | -11.49908 | -45.00765 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9543677b-25ed-3559-a47b-7f3bbff3aab9 | -11.21483 | -49.9513 | 2025-10-03 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d549d5b7-f6e6-3c6a-8682-7f4c8f3631ea | -5.48855 | -45.40471 | 2025-10-03 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a317173-d5ee-3621-91d3-97abfc63f991 | -10.26705 | -50.34191 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17d0c565-cd54-30a9-a2e6-97cc40cfffed | -7.78154 | -47.37571 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eeccd46c-dc6d-3410-878f-703210876c80 | -5.40226 | -41.33125 | 2025-10-03 04:32:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e9689316-c4c1-3639-8682-324b3f36f2b4 | -10.00737 | -50.2537 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c76b8b1-30d3-33db-9e3f-2b6ef6cd0212 | -7.75512 | -46.24334 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5b60ae36-3fbf-32d7-9406-bd326e04907e | -11.48549 | -44.98905 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25259403-d471-3e7a-abab-2f3f68b33ed1 | -9.91489 | -50.49808 | 2025-10-03 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2af6227f-3159-3d3e-b20b-bd44273098af | -7.25345 | -49.41373 | 2025-10-03 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e1c42a0-f0e7-3b59-a517-e38302aa0d61 | -10.28599 | -50.37549 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6dd1b6a-5d32-33ba-81ce-e69e896ae175 | -10.87429 | -47.82849 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f0ea1d2-0db4-3886-a4f2-ce73460a90d2 | -7.7557 | -46.23952 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5bf4091-0d3b-39cc-9989-0c0f9339d88c | -11.26997 | -47.79577 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ade42783-67d7-3e31-aa1d-773691d4001b | -5.91662 | -44.27191 | 2025-10-03 04:32:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebc8a74c-68c5-3deb-aba5-96a5b49c2f87 | -11.1347 | -43.41021 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| b112b960-1f7e-3cb2-9e64-7fcf9028242e | -10.83768 | -41.27825 | 2025-10-03 04:32:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f62ef10c-a8df-3d31-9f47-91de8ae15e58 | -11.27052 | -47.79221 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b3ce9a4-2549-34e5-82d3-879563b66313 | -8.16963 | -46.99956 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e506ff1-b84f-3a09-ba71-c5ed34ca9c3e | -8.80672 | -46.66903 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README107.md)
