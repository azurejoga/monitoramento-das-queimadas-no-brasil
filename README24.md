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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4899f903-16f6-30f6-ae1c-c4deb9784fef | -11.20756 | -54.8201 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 009f1c48-9225-37d2-857d-9a2db32b78ed | -6.71183 | -58.93345 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1bd14ba0-786f-3fdd-9a3a-d922ea56ffed | -11.11229 | -49.90829 | 2026-08-16 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e50e740-5e18-3247-a64c-357037dd14f9 | -7.36775 | -46.84237 | 2026-08-16 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 464a382f-6f1f-382d-a57a-ae8c2ba4a5ba | -6.83221 | -56.41052 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5df92c0e-0d2b-3d34-9b03-d816ec890fd0 | -8.61566 | -54.68055 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d63bfdc-afa8-311c-9d91-734e7ce07960 | -11.07101 | -47.27359 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 73b0eb97-ac1a-3774-bb78-5edaa2ef79d9 | -7.58344 | -60.88955 | 2026-08-16 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 032a5b1f-562f-35f9-a560-0d0190638046 | -11.32563 | -46.21888 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f9f1c05-bc93-312b-8212-5908fd48d856 | -11.80811 | -44.80923 | 2026-08-16 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 567a29b5-89e8-3cee-97d9-a6b2b91a6378 | -8.9636 | -60.52366 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c6fb98d4-c790-3389-856c-c7383b39c93e | -6.61481 | -58.98017 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b095dbf1-0dc0-384f-8da5-2856bca10e04 | -8.96857 | -60.52876 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4bb80abd-0f41-3d24-8a0c-48a3b723e84f | -3.5105 | -58.95053 | 2026-08-16 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3f4adeb-418d-3bb0-a8be-d61a247e0384 | -11.14235 | -49.04142 | 2026-08-16 04:40:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 042ed88e-1b0a-3a76-996c-86fd74ecae1c | -8.65542 | -54.73069 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| baf8d657-ceea-391c-a420-fabc811c2619 | -11.90094 | -45.96852 | 2026-08-16 04:40:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e7978ef-b13a-3036-be0c-05627f80ad12 | -6.59544 | -58.9949 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc61396b-9d32-3760-bb3a-411704640091 | -12.23189 | -43.13716 | 2026-08-16 04:40:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 74c68c02-37c7-3d77-bfce-c9b5ab836046 | -6.54708 | -55.17629 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d2035f2-55fc-3b66-909c-c492d408e71d | -11.06984 | -47.256 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ceb5d9e3-5736-3d83-b96b-4872eb6293bc | -11.5761 | -46.799 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fba29ef-bc5b-3622-ac1f-88285814fbb8 | -8.61229 | -54.70068 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3418418e-2951-3b20-97d7-4a1cd527232b | -12.01725 | -46.43292 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 94ed9316-06ee-3cd4-b2b6-585f52bbf465 | -6.842 | -56.4355 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c7c658ee-1cf8-3755-a9f3-b5f9d67275d5 | -6.28964 | -47.73559 | 2026-08-16 04:40:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9e00364-17d8-3e1f-85de-de86b2419785 | -6.61216 | -58.98274 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac2ef067-f353-3c6c-8a0f-42ac84aa4542 | -7.35588 | -59.59438 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e9707e8-a749-373c-a0ea-4d5e44fb34d7 | -6.82233 | -56.44177 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0d2bfba-520d-3fae-a6a0-336e9fa959e3 | -6.83802 | -56.43896 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6696b1fe-d275-3142-9f28-fa59154279ae | -8.9823 | -60.51867 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c141491b-ab29-33a6-9e62-51dfcc58feb8 | -6.61756 | -58.98372 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08742fb4-f9ec-307f-98e6-0c204f2d634f | -6.82576 | -56.45576 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2aee2ce2-f0c7-382e-a1a0-74e5f51e638b | -6.84983 | -58.96718 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e933dd1-e88b-345d-a021-51196b15d927 | -12.24253 | -47.0111 | 2026-08-16 04:40:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fbe3a040-ad19-328c-b029-6e22289d126b | -7.25774 | -44.69377 | 2026-08-16 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ecd7a16c-0f33-30f8-b72b-4b2f46a91bc7 | -11.20534 | -54.81009 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58d805ff-d6cc-36f7-932e-7697764f26c2 | -6.83293 | -56.43408 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cee4325-db8f-3323-af0f-32b4f1a180de | -9.30228 | -56.81395 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2d419b30-c622-35be-b7cd-cf67bbc4ee81 | -9.56993 | -45.37416 | 2026-08-16 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b1a14a8-4d5e-3580-9a24-9a9c665b5d91 | -11.62183 | -51.09148 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cebb64e8-6519-3064-a0a8-6c7d00b29c70 | -7.06538 | -56.64957 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c1efb4b-30ad-31bf-835e-c3aee4bab8dc | -6.6202 | -58.98111 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 357450d8-d1ee-3f61-9996-f84ed6e9ce25 | -6.70829 | -58.95383 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 650f9a68-5bb8-3c01-97e9-249f406a43d9 | -8.9793 | -60.53482 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab05d427-28e7-393a-be6c-be5e2664b810 | -12.46276 | -46.64939 | 2026-08-16 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0544fa58-9635-305d-861f-ebb93cdcd377 | -7.27574 | -44.72081 | 2026-08-16 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdaa2938-9301-37d1-9613-25567e2e9b8f | -7.11074 | -55.13032 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd37740e-c751-31a7-a1ec-7b3e648252ca | -8.43507 | -62.66829 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6228af0c-02a5-320e-9643-520e95d23979 | -12.46907 | -46.6601 | 2026-08-16 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46e9fb7e-3ea5-30df-8d7a-d32de66d3029 | -10.53533 | -44.84723 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48c9b015-7547-3113-9bb0-dabfa9d560a2 | -6.84176 | -56.44424 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2eabe119-382b-3cbe-a764-af315a013420 | -11.4367 | -43.91878 | 2026-08-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b55e5c3c-eea8-3257-933a-7ff616e76c70 | -11.96472 | -44.33301 | 2026-08-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09ac4d68-e8af-3147-916e-5bb48738a231 | -6.81547 | -56.45491 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c2c89d09-e434-3105-953c-3c41d3ed1b64 | -12.00785 | -46.42956 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7231272f-80f7-3886-a236-17c559b7d6d0 | -7.28026 | -44.71786 | 2026-08-16 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bb70039-3e08-3e1b-a642-0ac0e5e82458 | -7.40897 | -60.00783 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 404fcb35-a28a-3921-a031-1a410c86b956 | -6.85106 | -58.96032 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ada3e774-baa9-3a78-8eff-b785407b7010 | -6.62808 | -59.06183 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1024082a-019c-38c1-9c3e-76554ff31101 | -6.82495 | -56.46038 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c5c0dfe6-01ce-3af2-81f0-38dab4630cc9 | -8.96658 | -60.50773 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2e58e473-4233-39a2-a845-265b423f7668 | -7.83878 | -61.35336 | 2026-08-16 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1df0f55-bc28-3236-8eaa-1af75927c9b7 | -6.72615 | -58.93116 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bca7bd0a-a4d9-368e-9c41-40d420baa647 | -6.99283 | -45.91532 | 2026-08-16 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2d7068e-1c9c-3bbd-938c-c536fe858957 | -6.96461 | -59.3075 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 32c6bf74-a33e-318f-91c5-52887bc0d8e8 | -6.86691 | -56.40647 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fa7e1a3-0849-37e8-a0f8-62838e5bd078 | -6.63672 | -56.40221 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7247d288-e863-3170-9667-020ad5031a78 | -7.69143 | -55.15854 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35ab6b7e-9832-31b9-8c2b-80b493e354ae | -7.33812 | -59.60294 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 91e1ee96-0d0c-3fd1-85a8-0ba17f7fa713 | -11.50818 | -54.63113 | 2026-08-16 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e322dc74-a10d-32c1-a53d-630eb697a958 | -7.0094 | -41.4282 | 2026-08-16 04:40:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1e12ad41-f57e-3aba-ae6f-5c4e708435fb | -10.51706 | -44.85626 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cba7ee1b-58c9-3c1a-b338-4fbe61d4c745 | -6.83722 | -58.97571 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 611f90c0-f7d6-3bea-b4ec-924c62103ffa | -6.70414 | -58.9458 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2dd6b4f1-09a6-39b9-b939-cc09e4c321e4 | -12.02043 | -46.43839 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f008c8ef-b853-3c5e-9668-28bc5adf676c | -11.05531 | -47.25366 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fea49fe7-7893-3ca9-9d9d-641aa9e3ddf4 | -6.82534 | -56.45163 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c4f03902-a315-377c-8c2c-1e93d923e2fb | -6.59352 | -58.99406 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77b06e29-4a66-3213-88db-62ed98f56741 | -7.27673 | -44.71373 | 2026-08-16 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15501241-47a3-3f05-b82b-646117b3b575 | -6.8204 | -56.45969 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aad165c9-1e74-3942-8a7b-77138926f98c | -11.07225 | -47.26503 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2514d541-d351-364e-b456-f035467bd3f8 | -6.62433 | -59.08288 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fda30d7d-6205-35b6-97c3-90d9af839575 | -6.71954 | -58.93711 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| db70f54b-f278-3ba6-81e6-40fbf0f93835 | -7.41762 | -60.00428 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bf8e40f4-2b04-3c7b-88ea-7181952f049c | -11.82981 | -51.79812 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53199255-0e67-3cd0-8171-ca24d0566a19 | -6.72677 | -58.92772 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39bdb3e1-cdc5-3f2b-84a4-fbc43b24ba11 | -11.50897 | -54.62656 | 2026-08-16 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5aa83cb-3879-36cc-8308-e305a996c073 | -12.01976 | -46.44329 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 97e4c1f8-208f-36a2-9bea-c5364d276968 | -11.32629 | -46.21418 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 897a2d01-3091-344c-a190-30ff63d70038 | -11.87842 | -51.96093 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b4e5327-c0d8-3ce7-ab48-b1fabaed0e76 | -10.46034 | -46.30037 | 2026-08-16 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 155d3172-70f3-37d1-8fb8-c561b041b0cf | -7.35055 | -59.59742 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e01420e-a850-319c-9036-1e518e1136cf | -8.65216 | -54.72792 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 17e50029-9dc5-3a5e-a255-bac513064628 | -6.8147 | -56.45948 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9e105c90-c65f-3819-b0f2-92d2ecf4908d | -7.36714 | -46.8464 | 2026-08-16 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c766c3b-5a55-3fbe-9e20-95ad7375f5c8 | -7.08145 | -49.94422 | 2026-08-16 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04e85fb9-4ca4-3c26-a9f7-9cc9837b15b2 | -11.0826 | -47.24485 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f48b9da7-c469-3261-b147-9dda3c9e1b8a | -9.25162 | -56.90464 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1b59e76-6768-3344-abda-1e66c1d2b3a0 | -6.63164 | -59.07325 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |


[Clique aqui para ver as próximas entradas](README25.md)
