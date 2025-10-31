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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c0768c7-4528-35dd-ba65-2bc7b0e99889 | -2.6361 | -48.49911 | 2025-10-31 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f320b1c4-aeb6-33e9-8ec3-00bcbcd5ec11 | -5.18017 | -56.10892 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2237d735-24d7-3c29-b33e-c370ee389d92 | -4.55826 | -48.47746 | 2025-10-31 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 448c1726-1836-3051-be91-bac6158c90cf | -1.53576 | -55.86625 | 2025-10-31 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0bb3e3f-e659-3c5a-9dc9-8c202feb8181 | -4.87268 | -47.52573 | 2025-10-31 05:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e416f16e-be52-3cc2-b63e-1b2f8578f08c | -3.01522 | -49.45203 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 022e62fe-4fca-3264-bfb9-de56d133e75d | -3.87978 | -51.19453 | 2025-10-31 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10aa5097-e75b-3895-841a-27395dc986d8 | -2.90423 | -53.95592 | 2025-10-31 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99f92f39-d7c7-330c-b934-22978b733d76 | -3.94224 | -46.96905 | 2025-10-31 05:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23520351-acb5-3389-87cd-376e76773751 | -2.90362 | -53.95992 | 2025-10-31 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e9f4569-d056-32fb-8a97-b1d791456fb0 | -5.13516 | -55.96082 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cebc78e-14f3-360b-94f0-f611299d8f14 | -5.62646 | -47.11237 | 2025-10-31 05:25:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc891f4f-4064-3258-a792-037c97827b24 | -3.29378 | -51.91021 | 2025-10-31 05:25:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5fd74b0a-dd61-3130-8eef-a57371bc465c | -4.68148 | -50.44654 | 2025-10-31 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 400570ba-5cac-3f70-bf36-aedb7e90c9dc | -3.29274 | -51.91508 | 2025-10-31 05:25:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa760e03-6771-3297-ba0b-79b288acf852 | -3.29629 | -51.92759 | 2025-10-31 05:25:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7d8d75a-ab5f-3980-959f-fcddd513922d | -3.3288 | -54.08131 | 2025-10-31 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8a5d48a-77f1-33c7-ac47-6461654b2f60 | -4.67586 | -50.44587 | 2025-10-31 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42d25170-e95b-3d74-a760-b13da3fa1f6d | -4.47766 | -46.57053 | 2025-10-31 05:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9e11938-25a5-3634-b70d-a6553b3887e2 | -1.53508 | -55.87064 | 2025-10-31 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a689615e-c3ed-38d4-b3e3-75cf4ff38889 | -1.95578 | -47.85771 | 2025-10-31 05:25:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 834cfba1-20b9-3415-8d7c-0099a5889832 | -4.55196 | -48.4763 | 2025-10-31 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1efb9286-45a9-3fa1-b176-a031ef4d070c | -2.31055 | -48.58204 | 2025-10-31 05:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5a0c16d-5638-322f-85db-3db04986f9fa | -4.8765 | -56.02802 | 2025-10-31 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1902c76c-8b8d-3eb8-b4fd-ec4dafa1f088 | -5.4193 | -47.94097 | 2025-10-31 05:25:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b02ef2c-aed8-33f1-9f28-63aff3e5837d | -2.32208 | -48.58835 | 2025-10-31 05:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5be6863f-4dd9-3881-a935-39798736bbd1 | -4.6806 | -50.44115 | 2025-10-31 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4859af32-23c1-31a6-a2ed-13efd297c56c | -5.41849 | -47.94677 | 2025-10-31 05:25:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de84026b-d7e0-3753-a95c-e9867037cfcd | -2.09879 | -54.40204 | 2025-10-31 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e44653a4-7588-3740-ab32-7855397ee6e0 | -2.45264 | -49.01401 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5154690e-e130-30dd-a709-a3225d53c5f7 | -3.52782 | -47.5505 | 2025-10-31 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f7a55b89-9864-34ac-9a43-8007766ac945 | -3.44278 | -54.63599 | 2025-10-31 05:25:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 088972d7-2d4c-31f0-8739-c9fe7fd09d0f | 0.66806 | -60.30537 | 2025-10-31 05:25:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04a66b87-b355-390e-b9e5-821e144535b8 | -4.63918 | -49.48636 | 2025-10-31 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a276a7d-d738-3d9f-bab0-afdd5ac7bce3 | -3.29361 | -51.90947 | 2025-10-31 05:25:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f436f1a8-f7ba-3174-ae51-91e68b4180c2 | -3.30125 | -51.92826 | 2025-10-31 05:25:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 61c8aba4-5d8b-38f6-a300-ca0a1ba97bc3 | -2.64152 | -48.50185 | 2025-10-31 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba558b20-0cda-3c8f-83da-7680c2dbd60b | -3.54009 | -58.65122 | 2025-10-31 05:25:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51f95c77-c9e4-3ff7-b7c0-fb4149fe6f17 | -2.91339 | -53.95326 | 2025-10-31 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 111b885f-df38-3f75-ba3b-76bd269c49c3 | -4.63857 | -49.49062 | 2025-10-31 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9c8d4e0-4c0a-3486-902b-1262b3c6f2ad | -2.63536 | -48.50088 | 2025-10-31 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 793f7d82-3b2a-331c-a6c4-9f5e3e4190f0 | -5.62571 | -47.11782 | 2025-10-31 05:25:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 065af4a9-b1ae-3d68-924c-0437aa4b83d8 | -2.42175 | -49.30188 | 2025-10-31 05:25:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3053e70d-96da-33c8-a818-11d1b2b63ae7 | -2.63467 | -48.50556 | 2025-10-31 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 262f2306-8e14-3a70-a9d1-adabb0381fa2 | -3.02016 | -49.45063 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ae265932-48bf-384b-a4ae-9720dc20c304 | -4.55756 | -48.4824 | 2025-10-31 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d610b6f4-d9e7-3928-a1dc-2fe1916d4c97 | -4.05646 | -47.50025 | 2025-10-31 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16c8f6e6-1693-35a9-9a33-6efaa970732c | -3.54673 | -58.15947 | 2025-10-31 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2341d1d-5072-35ed-850b-80d9bf3861b4 | -3.32512 | -54.07679 | 2025-10-31 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c5cd7a9-7ad6-3f57-a543-8a659c637ec4 | -2.44663 | -49.03557 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1da3365c-111f-3483-a57f-0259b4efb2ec | -3.02105 | -49.45291 | 2025-10-31 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8dec9fd4-4ea7-3562-a755-f813be209afb | -12.431 | -63.1294 | 2025-10-31 05:27:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f4ddc9b-6d7d-32f9-b8b1-b7e4edb4e906 | -12.22338 | -61.3456 | 2025-10-31 05:27:00 | NPP-375D | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 730262ee-7f0c-3b1f-9f4e-171c5569f14b | -11.74239 | -59.31033 | 2025-10-31 05:27:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82ea966d-442d-3787-a7a0-70dd373b78dc | -12.29129 | -48.06527 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 58189ab2-74c2-38e4-a4af-3dacea47f774 | -11.15221 | -50.72564 | 2025-10-31 05:27:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b6f78e0-5334-32fc-a06c-c0614216be69 | -13.23456 | -54.36164 | 2025-10-31 05:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c43b34d0-816d-37c4-b05a-01c23753b5d6 | -12.1543 | -48.00645 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed60e4bb-71ed-3141-810c-eae0c4628b49 | -11.12687 | -54.64693 | 2025-10-31 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7b3d617-2034-35b1-b73f-eb85fef1774d | -12.27167 | -48.04575 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d84387fd-3341-3c98-854e-5426d74064b9 | -11.9935 | -63.95005 | 2025-10-31 05:27:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 479066d1-a130-3e22-aa7e-585e5e00b26d | -11.12286 | -54.64158 | 2025-10-31 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aea54d5e-8f24-3ad8-85fa-9bf5fefa5079 | -12.04719 | -54.24822 | 2025-10-31 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88481992-5630-3de4-a57b-0c163570a6a2 | -11.72894 | -59.30417 | 2025-10-31 05:27:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42e7513c-8d98-3145-9990-a89d82082817 | -12.28427 | -48.0633 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 255adf91-56f7-3962-b362-d9c507924c0a | -12.15777 | -48.0055 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2df80dc4-dbb1-358d-b1e3-5f0028a4a0f4 | -11.15276 | -50.72117 | 2025-10-31 05:27:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21d3eb5c-7d94-3fe2-b5f3-386f5035fd9c | -11.08038 | -51.54377 | 2025-10-31 05:27:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1cef76a-1cb8-3322-8be4-f8309dd21906 | -11.15167 | -50.73009 | 2025-10-31 05:27:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51172cc4-2db2-3439-8378-9698a6cc7247 | -12.27618 | -48.0487 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 73b49a94-90c3-3841-b4a7-4b1d1347c786 | -11.12795 | -54.64538 | 2025-10-31 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18fcd976-40f3-35b6-8e89-52ae5a4b31d3 | -13.23039 | -54.35558 | 2025-10-31 05:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14015da3-9f59-3e37-a8b9-2bc77f2503fe | -11.73245 | -59.30472 | 2025-10-31 05:27:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb3e892b-08ab-32e5-99e0-5a1d29ba3c69 | -13.22622 | -54.34943 | 2025-10-31 05:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b423781-58c2-305f-98c4-a900d7bd2df9 | -9.51305 | -47.27018 | 2025-10-31 05:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 939ccd42-ff02-36de-81b8-8055e59a9ef2 | -12.15702 | -48.01254 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1d0b3b1-1ae7-3a14-a6f8-f723f002ed69 | -10.63643 | -52.18185 | 2025-10-31 05:27:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0603fadf-8745-33a4-b87e-8866f28e531a | -10.53493 | -53.71081 | 2025-10-31 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4efbbfd6-d4e1-334a-b126-0e153921f40d | -12.27871 | -48.04761 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6f3bd13-a45a-305d-9955-4ea696d5dcd3 | -12.61993 | -62.03376 | 2025-10-31 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2580d46-e790-38db-b286-646f03e8fadb | -12.15352 | -48.0134 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93a07246-c273-3fc1-82cf-064a83962397 | -11.30996 | -51.44987 | 2025-10-31 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f6de397-1f39-332c-b645-7edfbfae0b5c | -12.28361 | -48.06941 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cc8abcb7-eb1f-355e-bec1-1703bec6bd33 | -11.15767 | -50.73087 | 2025-10-31 05:27:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 629c90b0-76b6-3df2-ab00-e046a9f76992 | -11.94417 | -60.48389 | 2025-10-31 05:27:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4835d72d-b3df-3ca8-ad27-5a99f97d7a3d | -12.28577 | -48.04929 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3d0ee9c-d3d9-3bba-b9d4-f01b084abc8a | -11.2908 | -54.31413 | 2025-10-31 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ae8942e-edd8-38ce-80d6-f8f5b02d8490 | -13.23594 | -54.35069 | 2025-10-31 05:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c87bdd29-34e6-3008-9dd8-e4d3fc531689 | -9.51822 | -47.27233 | 2025-10-31 05:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8244fdb-1aa2-396c-b460-3d88ae1b3123 | -11.12332 | -54.64482 | 2025-10-31 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43d5805e-95b5-3519-afff-f619fc81c650 | -9.52029 | -47.27115 | 2025-10-31 05:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68a83e3a-8118-356d-ae97-9d829e28f20e | -10.64142 | -52.18601 | 2025-10-31 05:27:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be1f9b58-f5a2-3701-8e46-4656616c654a | -11.07989 | -51.54767 | 2025-10-31 05:27:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfb0c005-acd6-3e88-a445-20b21896c8c3 | -12.1414 | -64.28106 | 2025-10-31 05:27:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9aa7bb98-6d03-3a0a-a9ea-c91628df3c00 | -11.12749 | -54.64214 | 2025-10-31 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcbf078f-8163-3c00-b1a5-8257b910cd8a | -12.04238 | -54.24759 | 2025-10-31 05:27:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e2522a5-da14-3090-b797-6bba6071c3a2 | -9.63031 | -67.20983 | 2025-10-31 05:27:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfc03bcc-6554-37e3-ae2e-62c38a9722c1 | -10.64098 | -52.18944 | 2025-10-31 05:27:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb5d72c7-2a37-364b-84f5-fa4931a2552b | -12.28168 | -48.06394 | 2025-10-31 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 089b5419-e378-3381-a34e-ad958ad00dad | -11.73596 | -59.30527 | 2025-10-31 05:27:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README43.md)
