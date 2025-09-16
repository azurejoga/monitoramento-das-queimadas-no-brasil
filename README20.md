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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 631f9a90-f90e-357a-956c-3d16cc108349 | -10.71556 | -46.48374 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 842297cc-0173-32c4-8e58-b8bf1805e6e2 | -6.50478 | -43.19552 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2736befd-6d07-3ad1-ab21-189c1a189c9c | -5.47983 | -45.34848 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc2ccac3-6d8a-3f61-802e-ccc74e4a0c36 | -11.42472 | -46.93567 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 496c43bd-3746-3338-821c-0f8ae91f2633 | -6.17603 | -41.21904 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b60a0c54-5710-32d9-846a-1ac2fa84041c | -6.82471 | -47.83119 | 2025-09-16 04:02:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b6144d1-6886-3853-a5d0-0ab9ccb08867 | -6.51315 | -46.21497 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bb17893-6571-36e2-aad7-2d02928aec62 | -7.67862 | -44.49124 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f331416-7b06-3c17-a861-ee4fea364e63 | -8.14029 | -43.64662 | 2025-09-16 04:02:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a97fe090-fdc1-3e53-8a2e-23d471c50110 | -5.90069 | -49.10286 | 2025-09-16 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45fb2a21-266a-3545-9816-3433461e906a | -7.54624 | -43.99596 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f49d35b7-01c0-3461-ae00-62ab1d7547e8 | -11.48815 | -43.60822 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2727dc2b-185f-358d-893e-4c7f3174aacf | -9.09851 | -44.85823 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 8c32dfd7-79ea-3a15-8f09-99afea7b2ea1 | -12.11201 | -44.8156 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6dfb37c-5e42-3174-9704-01af9e4a67b1 | -8.92922 | -45.52258 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d8a021fe-493c-3eb0-9ee9-0b5cdfaaddc7 | -5.05331 | -43.10141 | 2025-09-16 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3fa19469-5c1a-362e-9c61-7ea7f6a4844d | -7.25604 | -44.59464 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b86c2a96-6e52-3753-997e-b4a3b4f87998 | -10.6436 | -46.46002 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb9a8a29-0950-3b87-a3ab-f7cbd001e060 | -7.66001 | -46.60244 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 845228fe-d4f4-3525-b583-26086f4208b2 | -8.58471 | -46.351 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b3faf93e-91bc-3ecd-863d-8ddac0eef8de | -5.34953 | -44.81649 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6336021-dbe6-3f85-80b6-c86b6e33b2c4 | -11.12177 | -45.33846 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7a282a5-8e32-31b8-96e9-2a7b01a021ca | -11.45773 | -46.92587 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 400c10cb-5ccf-32d9-9782-c186d5c144e1 | -6.4299 | -43.31549 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d57fef0-b398-3e0e-bf12-572c89708d29 | -8.90157 | -46.15431 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87acf7c0-9754-3831-9a68-8fa8f38f5acd | -7.27926 | -46.58246 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4ebce076-90c3-3e9d-9638-1a6ed3e2e8e8 | -7.97777 | -45.63476 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d6be9a2-8e88-3239-ba81-ff70e803bd1e | -8.43337 | -47.21437 | 2025-09-16 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27ac7bac-0692-3160-83d4-1b104d857ad6 | -12.17547 | -43.57832 | 2025-09-16 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc0b7966-bffb-3b75-a9d1-6dc6390e2679 | -11.4383 | -46.93817 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cc1e2669-d902-331c-a3c9-838999902bbe | -7.43308 | -45.83744 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bbcc503-6d5b-3ab4-8c02-ea1bf4f0750f | -12.2662 | -45.29612 | 2025-09-16 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38d2258d-e390-3970-bb7e-cbcd7d17857f | -8.42966 | -47.20911 | 2025-09-16 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6a5d74a-0c59-34e9-b1da-f4047167a3d3 | -10.94517 | -45.50344 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87986ad8-0f9f-3294-ac8f-7bed6ca28137 | -8.39789 | -47.25943 | 2025-09-16 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c09029c-eafd-3b2b-beaa-a9b621565952 | -5.54446 | -46.41198 | 2025-09-16 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 557c1e57-97d1-3e10-b5b5-ca5c59f849c2 | -8.83187 | -44.21422 | 2025-09-16 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be848457-e047-30cf-9a80-56d12953dc31 | -9.09283 | -46.93416 | 2025-09-16 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14ce867a-d530-36c3-a01c-7409a17309df | -6.76172 | -44.72464 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0dfe8426-38d2-39fb-9c56-73285bafa89d | -6.50653 | -41.81844 | 2025-09-16 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9409f3ab-e804-3cc4-8e10-5d599b3d0810 | -7.5493 | -44.02375 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd2f67ec-a755-38e9-8198-ec71d7f7a1b4 | -5.91334 | -42.74232 | 2025-09-16 04:02:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7df8125c-4b9d-3adf-80b8-77815b4823b5 | -8.95972 | -45.7664 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f7138f9-767d-3930-8f71-0751120cee1e | -6.29477 | -42.3994 | 2025-09-16 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 939f7021-2e53-3ce2-a741-116988c3910c | -7.5621 | -50.46017 | 2025-09-16 04:02:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 356bb144-d112-3edb-ae19-c7dfb35710e7 | -8.93153 | -45.50889 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9388b8cb-1009-3629-bcf4-0a29198ca915 | -7.06253 | -44.17329 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b0bbd460-0eb4-3b1f-bd06-6907a27fbbad | -6.5552 | -43.99588 | 2025-09-16 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 07abc1f8-bcc3-3f2a-99d3-67553a6da675 | -6.25923 | -40.62537 | 2025-09-16 04:02:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c5ca5428-61f9-3098-9e70-036cb14772e8 | -8.00299 | -43.82035 | 2025-09-16 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e4584fe1-f044-318c-8504-7775a5a71028 | -10.78831 | -50.65331 | 2025-09-16 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddbfab51-0672-3248-9cad-dc4a40d78313 | -11.50413 | -43.72771 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 357a3d24-69ae-3961-a3b8-98c8eea55b65 | -7.27041 | -46.60753 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89fa5f49-7f8d-3f74-9303-279259588625 | -6.18548 | -41.17733 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f71eaf64-8c97-3282-a360-0d3b0eb875fb | -7.04598 | -44.13348 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 646dd2ab-cf94-31ae-92cf-257c5c95a2bf | -5.2826 | -43.21458 | 2025-09-16 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e87dd520-d62a-3fd5-846e-152b8bc15451 | -7.26397 | -46.59272 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b40c87fd-e57c-3df7-81ea-97ebeb9124bc | -6.96947 | -44.56844 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c259a33-569f-345f-a482-c6d1a8678197 | -6.63299 | -47.88542 | 2025-09-16 04:02:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25202324-a0bd-3e47-83b4-0299caf11d1f | -11.11197 | -45.32714 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 521d3304-4c5b-34ed-a67d-2331149029d7 | -5.09848 | -43.82757 | 2025-09-16 04:02:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 038e84ba-b23c-3cdf-9066-63f17f0241d9 | -9.09933 | -44.85342 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| f08ec65c-c910-3816-9a79-da6892ad92c0 | -10.72544 | -44.76742 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84e8263e-6f56-35fa-a31d-c8e20b90ffe7 | -10.71544 | -44.76764 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d55e08f-f0f5-3786-bfda-082250a167f7 | -7.63179 | -42.31925 | 2025-09-16 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fd01298d-5ccc-3245-96f3-a54b53f00194 | -5.09814 | -43.8291 | 2025-09-16 04:02:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 52a86e1c-1a6b-38f9-bf44-82ca6f2e0d33 | -7.08955 | -39.67084 | 2025-09-16 04:02:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| bac33681-5dd3-37cc-9748-cb7fdd1fcfeb | -9.06961 | -50.30507 | 2025-09-16 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78526e1e-32a3-347c-9829-b1c8d18ca801 | -11.13397 | -45.33564 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 934e7d4e-54e0-3fe5-8ed7-4dee3caec0dd | -11.29808 | -50.85028 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 563225f1-8dab-3517-96b1-563645bf6151 | -8.96163 | -46.02567 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1398f72a-6a42-3800-8aab-31e055bdbf57 | -4.17802 | -48.57304 | 2025-09-16 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82e3b8b8-cad6-3f4e-9c1b-771665707908 | -7.27551 | -46.60412 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bb8c5c6-bbff-3bb8-96c9-02f08ccaefa1 | -13.61656 | -47.64291 | 2025-09-16 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 864342ef-cb6f-3b56-a87c-3d66583cd868 | -12.79259 | -47.26109 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 09a63b5a-7218-3d29-96aa-2d2690c39156 | -14.82194 | -51.66629 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9739cc7-b56f-3637-a4f2-2b2ed54e2093 | -12.66638 | -48.02035 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed7536f6-0196-3c5d-a26e-08905cabfe87 | -16.24124 | -48.15083 | 2025-09-16 04:04:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24c6ee82-a0e8-3f6a-99bf-b7899d3ecec8 | -12.95768 | -47.96391 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5f5e7d53-edab-33cf-a4b4-c5d93572deeb | -15.78736 | -53.44596 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b7351afc-e7f7-3c2a-b83e-bc3f5ec532c4 | -13.20607 | -41.97906 | 2025-09-16 04:04:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cd471142-91fc-30ab-9d4b-f420d14a4ef2 | -16.52737 | -43.73061 | 2025-09-16 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7825d22-efdf-388a-a67a-cf7e67a9af9c | -14.61991 | -46.37984 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be5855b2-06e3-3822-bec9-179366bdbf4f | -14.52086 | -47.33061 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 647bb6c0-30ef-312b-a44d-6bb2c10cd044 | -17.59291 | -46.67347 | 2025-09-16 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e03bd6d8-fc2e-3b13-a06c-5e0ff1eb4191 | -13.51622 | -44.29942 | 2025-09-16 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b735289b-2ff5-3ff5-9b8b-01bf2e8f6abd | -12.66178 | -47.71888 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| e673c568-61ca-3bb4-8e53-bf74379f1f93 | -14.51264 | -47.3755 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef2545ed-915b-3c80-9b29-1e45ff57c740 | -12.80458 | -47.24255 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7469ede0-2761-3069-81ad-809b7e83d2c9 | -12.68797 | -48.00163 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6fac5784-e62f-3c4c-8a62-e5de9366ab4f | -16.69346 | -49.77891 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a02db71e-c3ba-3c9a-9598-f5c056068318 | -12.78992 | -44.74755 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10af6a61-486a-3625-8b0c-64675338dbd7 | -14.86459 | -51.62044 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd14d22b-5b74-3345-b2ea-5e54d5c964ae | -16.8129 | -47.78524 | 2025-09-16 04:04:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96d2a5cc-6e17-319d-83b5-3291fa11b2c6 | -17.86706 | -44.44406 | 2025-09-16 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 77c56cd5-b266-3837-a510-901faf54c564 | -13.96051 | -44.77411 | 2025-09-16 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 811846a1-b74e-3b31-b458-a727d47035b0 | -13.01056 | -47.9507 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85843560-e8d8-3ba8-9112-c8a4e90f47ec | -12.6098 | -47.95673 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ed48ae9f-10c3-3a32-be5b-8c7d2b2648fe | -17.08007 | -45.82976 | 2025-09-16 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 792516e0-6725-3f7a-ac8e-dad6cd804d70 | -12.86016 | -47.14819 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README21.md)
