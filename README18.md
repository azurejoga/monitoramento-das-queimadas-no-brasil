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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cde6ceff-d781-3eb2-ba28-c14486972c25 | -11.28906 | -45.00982 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 986c60e6-b0ee-38b9-bd85-756dc7c24e76 | -8.38444 | -47.74561 | 2025-10-29 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba124eba-6735-36a8-9962-5ad35d5e6a70 | -8.55559 | -47.01141 | 2025-10-29 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f935f22a-aaf8-352b-bed6-b8534d96205e | -10.76835 | -47.89584 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2c318e1-056b-378f-bbe0-ad4666112690 | -13.86919 | -48.48497 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e2bf6829-d986-39b6-a507-a31c470442d2 | -10.52081 | -44.2069 | 2025-10-29 03:55:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b842831-00af-389f-ba5d-cc5cec145e9c | -13.57176 | -49.60638 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5972ee36-8643-3721-b082-468e455dc084 | -15.4326 | -46.27187 | 2025-10-29 03:55:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38d32009-e653-31ea-8a6a-76bb7709bcfd | -13.47126 | -47.82137 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d4a6dd3-3d53-3b30-a9f1-9dfe33e683dc | -10.50979 | -47.73412 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 97f80261-3eb3-3d03-9c76-07b0a07c4dcb | -9.92717 | -47.67938 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 321f11e2-6c22-39b4-aede-752bc62feaa3 | -13.57916 | -49.60627 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8abf8864-548d-3385-9f0c-b2bf0d339960 | -13.91456 | -48.46337 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba6676b4-a36f-347d-bef2-c2d4dfb09b8b | -13.32175 | -47.4363 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2cdb21f3-c894-32c7-9368-425002d0bb0f | -9.80484 | -47.75733 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7319dec8-e581-3463-98b8-ed31f960bddc | -13.64198 | -46.47042 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 637b0458-3bba-3323-8481-ea4c5d710da7 | -10.93538 | -47.80748 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae41c939-c688-382b-a1a0-089beef04e22 | -9.27569 | -46.3859 | 2025-10-29 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 099c83bc-e12d-3987-80fc-19b60677df29 | -12.97886 | -47.91411 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| defd1bb7-98d3-32aa-8ecf-17bce21c7a5b | -10.55226 | -44.84175 | 2025-10-29 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9d9ad1e-7ce8-3840-96a1-98e85359ade1 | -9.87857 | -44.88316 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42408652-c49f-3ce6-a365-dc718d28ac16 | -13.65326 | -48.45025 | 2025-10-29 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7d7f96c-5daa-3054-be41-af78301fc121 | -12.08981 | -47.25196 | 2025-10-29 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f3379b6-2c28-33a9-9aaf-3e344460482d | -9.93764 | -47.86728 | 2025-10-29 03:55:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1c44ac2-2fd8-364b-906b-ad99c46e98fa | -13.03785 | -46.73195 | 2025-10-29 03:55:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b2ff0f7-a069-3d5b-9636-20b9d83afc38 | -13.60805 | -46.48427 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4e0d106f-98ba-3b64-af80-fe52bd074cb1 | -10.85998 | -50.10303 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d0372dd3-00c6-3b85-beef-6741961f27b2 | -9.23209 | -46.35006 | 2025-10-29 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ebbef36-e008-3389-a421-afb24979e5cf | -10.51149 | -47.72493 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 651747e4-14cc-36a2-97bc-a0a5bc959183 | -13.23746 | -47.06326 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ce709fa-2bf8-3a83-be42-b08b55cf71b7 | -13.30993 | -47.46643 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ad534ce1-4c5a-3250-87a8-c22710fc43df | -14.88698 | -46.75953 | 2025-10-29 03:55:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bda0675c-f33d-370d-8517-93b85904a6a1 | -13.55317 | -47.35332 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c2d8543d-101e-391c-b542-924f372939f7 | -12.5 | -42.895 | 2025-10-29 03:55:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b4039251-3bcd-36d3-9433-d1070ea09f70 | -9.49039 | -47.00476 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 925aace7-7d07-3bda-af3b-c1b79e5d5066 | -16.67515 | -41.35193 | 2025-10-29 03:55:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 39e6bf81-b0f8-3b77-8c93-bd9e080a57b3 | -10.64945 | -48.00764 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2196752f-1ba1-342c-9a4f-cd3ce8cf754b | -10.03172 | -47.13394 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 59ce53be-7f9a-3753-b921-5ce3ac2c0383 | -12.98388 | -47.91443 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b42a601b-0d2c-356c-9aed-d606993c7961 | -14.32301 | -46.51949 | 2025-10-29 03:55:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f501d3f-8906-347c-9ce8-d536d6cb8dd8 | -15.17988 | -47.20941 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91937145-4d5b-3798-8a52-b0466e5bd677 | -15.0985 | -43.84194 | 2025-10-29 03:55:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c5654705-99b6-3ebe-8ccc-714ce9e25a41 | -13.57025 | -49.59471 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b85f02da-8f0b-3f0e-bd0b-59fbd36f0259 | -14.67938 | -46.35999 | 2025-10-29 03:55:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 822beac3-a3d0-3991-957a-c51d2078cde5 | -13.66479 | -47.18301 | 2025-10-29 03:55:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97a5ba74-7dfa-34ec-8f79-3ca0ed79262b | -15.45934 | -47.68655 | 2025-10-29 03:55:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91d071a2-5e02-3bc9-aec9-cb24bab79677 | -10.90927 | -48.005 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8378552-41f7-3d4f-823a-4c4c84082d14 | -9.15337 | -46.40174 | 2025-10-29 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c35d265e-5af7-357e-aa7c-5a4aa400ed96 | -12.07892 | -47.99404 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 981ead7a-7f07-3170-bc2d-13944fa7c56a | -13.20777 | -47.0688 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5606185a-4fa0-3e20-8a7c-d0e4db83e6f9 | -13.94463 | -48.46864 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84b7fdad-991f-3118-b7e4-b7e659f518cc | -13.5585 | -47.3245 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c3d296c-7de7-3495-9df5-edfa94d7ad68 | -12.70579 | -46.30555 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f6e47edc-2559-338f-b564-f53dc81e8033 | -10.51093 | -47.72796 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffa3c605-47db-371a-9413-500e6712b268 | -10.35517 | -47.5649 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 542e9e77-0280-3916-bb4d-5e3fa5ed9a76 | -14.47714 | -45.25477 | 2025-10-29 03:55:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59656ba1-ab52-3e4b-8ce7-af0f1b670351 | -10.367 | -47.13799 | 2025-10-29 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55b28e3e-d322-3807-92fd-444817ccb5cd | -12.07782 | -47.99987 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57b65c51-e63e-39d8-a948-20b6f5132720 | -9.87876 | -44.88227 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2cf007f8-6d10-3147-8ac7-e720c6676689 | -12.70141 | -46.30446 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f6a4e0cf-4c1f-3976-87df-7801be3d1403 | -13.375 | -46.63413 | 2025-10-29 03:55:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da4e6086-d09a-383a-a02e-0bb9bc5544a8 | -10.74469 | -44.75504 | 2025-10-29 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a3cc292-7e52-39a1-9a30-2a99c17daf13 | -14.51944 | -48.00333 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 94f449a7-8518-30de-9d4e-2ca69f9100f8 | -14.5206 | -47.9954 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1e369a1-65cd-3da4-9598-51453748cd57 | -13.57254 | -49.60234 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 026af727-18b6-3d64-99db-f41a00d00d79 | -14.49852 | -47.87894 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e00a6b93-a81d-3ffe-93e0-7c624a2cc074 | -13.63192 | -46.52433 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 842856ef-567d-317a-90f7-3a0607be1d26 | -13.62357 | -46.47144 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fe03eb14-9ae9-3eff-b1d8-617d2c9734b1 | -14.89053 | -46.76478 | 2025-10-29 03:55:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1daa6016-3948-30f6-98cb-e4796981586a | -13.63275 | -46.51987 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b1929a25-0fba-3169-b207-170e50ea9f40 | -10.50478 | -47.73288 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3921fcb3-bcd0-3c73-a912-a25b3448f7e6 | -10.51598 | -47.72891 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0278759-becf-32b3-ac91-083062e02e89 | -13.23109 | -48.56649 | 2025-10-29 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54e97ba0-0238-3015-8b60-61bf75535668 | -9.49258 | -47.33953 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d777f346-b6e4-3303-94e7-46ff00e5c090 | -13.8635 | -48.48756 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e154e93-9392-373a-8314-40fbeac9c3d8 | -10.77146 | -44.62446 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 32d8f760-23ee-3260-b867-6b3625a298a5 | -11.25942 | -47.8153 | 2025-10-29 03:55:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e11eddd5-8e18-3616-8d6d-954fe7e530dc | -13.22647 | -47.72759 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1f2a3786-b639-375b-8e30-b2958674bf37 | -13.23309 | -47.9987 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 647850b1-3672-3019-aa61-d1e9bf3d2a78 | -13.86301 | -48.49014 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a6fb947-0ff1-344b-bab2-c974b1c17d0a | -10.9214 | -47.60471 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebf43830-d363-3fd3-946d-d8ee16396f19 | -10.76893 | -47.89277 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f82daf8-73b2-31ef-9ea0-6b90df24ccc5 | -13.62454 | -46.46854 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c65e5cc5-2bed-39cb-8490-4b06c352fe19 | -9.0669 | -48.72137 | 2025-10-29 03:55:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6ca20e1-72a0-37db-bbcc-aebbbb678765 | -11.99748 | -46.78593 | 2025-10-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 10b9b64b-dfea-381e-a72d-1796383186fa | -15.16672 | -47.22979 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9d31730-626f-3464-acb2-caa12827687a | -14.48114 | -45.25552 | 2025-10-29 03:55:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cc89b71-df61-382f-bca6-387938d6a302 | -13.36146 | -43.77135 | 2025-10-29 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a265fdb7-2775-3131-ab87-464a219ba810 | -10.48997 | -43.33041 | 2025-10-29 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d20b579-9236-339c-b181-bd3361d72a2a | -11.14897 | -44.93373 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1e93ed4-5161-30b9-aeac-20fcf0c6999a | -12.86928 | -48.63002 | 2025-10-29 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a42aebe8-12ca-39a0-a6dc-d7548fec22fa | -9.92958 | -47.68253 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b518b82-0de2-31d8-96d4-d0db33de4812 | -10.64552 | -45.2498 | 2025-10-29 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b5e0875-3fda-3c95-a6db-c58b86f9631e | -12.87377 | -48.63449 | 2025-10-29 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b4fcf14-3867-3b63-bdd5-e0246cbc7f9b | -9.95449 | -47.15718 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 151a1e1d-e5d4-3b79-a249-4e699bf5788d | -13.33142 | -43.18528 | 2025-10-29 03:55:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fc316851-d3e6-35e4-91ee-2026a01483cd | -13.64282 | -46.46591 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aac65b89-c946-309b-84ee-b66954111f66 | -10.76443 | -44.73919 | 2025-10-29 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f211b16-f01b-3d16-8b3f-29e20b7d51f5 | -14.24209 | -48.10719 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6172ad06-8427-3c40-917e-87f67aa55f6a | -13.22544 | -47.07646 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README19.md)
