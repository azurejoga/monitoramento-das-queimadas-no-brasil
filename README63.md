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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c781589a-e409-3d24-97b2-18d25a15f778 | -5.97395 | -40.91242 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 32d447a8-a2e7-3f20-b2fb-013311b0b818 | -7.07111 | -40.9394 | 2026-10-08 04:02:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 08836241-ad5f-368c-b2cc-269eed6d9950 | -8.06053 | -44.81091 | 2026-10-08 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8da6d191-6761-38a4-a402-ed852f4db499 | -7.06009 | -40.9416 | 2026-10-08 04:02:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0d3910c1-8d7c-3346-bfb7-2df00a4b471c | -5.08542 | -49.70401 | 2026-10-08 04:02:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8620613d-3daf-3e64-864a-19a34ea37186 | -6.37114 | -42.90552 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e1af09b5-8941-33c2-9beb-5dcebcad58fa | -5.98892 | -40.93065 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 53a5c22e-f337-3709-9791-6a75f0eb0724 | -3.20623 | -50.55629 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 03607fb0-759a-3ccb-906c-6e6634a4b048 | -7.27953 | -45.57479 | 2026-10-08 04:02:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bdfe258-7c86-35ef-807c-8b349c31e90d | -6.13854 | -47.93846 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1954f13-65f9-3d56-8499-a578d9f99c0e | -8.71245 | -45.2037 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ae780cd-4a52-300b-a52d-a900c5a91327 | -11.25685 | -45.18553 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d69d475-8a41-39a6-94db-346db097a4d5 | -6.33226 | -35.3596 | 2026-10-08 04:02:00 | NOAA-20 | VÁRZEA | RIO GRANDE DO NORTE | Brasil | 2414704 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| b83be77a-81e5-35cc-9327-b8e5a8070556 | -6.32867 | -43.35004 | 2026-10-08 04:02:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2699bdc3-8c3e-3727-9a77-136fc7cd0429 | -11.00123 | -45.42941 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02d92c08-d9a1-36cf-ae40-7b835004729c | -5.48415 | -42.84466 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10392f2e-d42c-3704-b85a-74a43f574aef | -8.73338 | -45.1603 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ab520435-7c6f-3a05-bda2-9a70a486b99e | -6.96948 | -40.37446 | 2026-10-08 04:02:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b8f93c24-16a4-3cc8-b306-770f2fde7b70 | -3.17024 | -50.60522 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2023f372-fbee-351e-8fdf-3646aceb5628 | -9.82502 | -44.78639 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d92d1ac6-d3ff-3bd4-9b0d-1960799c3e9c | -10.30237 | -46.60501 | 2026-10-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6ea6c9a-c114-3da8-9514-284fd90c9842 | -9.94794 | -45.9718 | 2026-10-08 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98622517-b7d3-3ebd-a29b-3a408b47b1e7 | -4.14684 | -47.98851 | 2026-10-08 04:02:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cfb50bc5-741c-3f24-9a68-e6f521ff65ab | -8.71968 | -45.18781 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b17ee0cc-8be4-3522-ad42-e1111eecd9e2 | -7.34973 | -43.18564 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 18f0d510-e7f4-38e8-bfd6-efc2c1c18b49 | -6.1459 | -47.92866 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| b255fda6-bd45-32e7-818b-a5f3558c4d77 | -6.15155 | -39.43415 | 2026-10-08 04:02:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 126cb3c5-d7fc-384b-b3ca-b2b8332fb369 | -11.23937 | -46.2543 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2b88bc62-1d70-3918-bb76-5eaca32286d6 | -11.63128 | -43.6916 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2d7ab1fa-3251-3105-8a2e-57de5e60c387 | -5.71146 | -41.7623 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d77094a2-8347-323f-9a61-0bca4cf4f862 | -8.38054 | -46.29172 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0114a247-fbb5-33b3-bb45-c6454b68b8c0 | -8.60176 | -45.63367 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84c9190f-9102-37d5-827a-06bb671abfdd | -5.48238 | -41.21609 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1c27ec10-4025-39fc-a7b2-71e9a536ccab | -6.8888 | -43.69591 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7e8b8b7a-64ca-3129-a1d5-df4826bf9daf | -4.3454 | -43.79457 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 2a7af94a-ed4b-356b-9c0a-383d0cb85b9e | -6.16368 | -39.44 | 2026-10-08 04:02:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b01de2b4-cf73-36ae-b3e9-814d2136ef9b | -11.22361 | -44.87256 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e064d717-3001-3860-b5c2-8d7a7654dfab | -3.34914 | -50.48457 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f3f3024a-6190-3ffd-8900-a11b1ad29cf6 | -8.98318 | -45.91756 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25779c28-5dee-39f9-b9f5-c467ae1d664e | -7.22079 | -44.15606 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41deeca8-0f7b-386f-b29a-6ba9463b5aea | -5.73406 | -41.76169 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 57271811-b254-3564-b513-e7605477c94a | -9.8068 | -44.7795 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c2822da-72c9-3b33-8118-936098eecc8d | -10.77228 | -46.53798 | 2026-10-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d40b51eb-fdb4-3e16-a7d6-f04798887e4f | -7.22827 | -44.27328 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4af8590e-899f-3a47-a071-1568e4ca511f | -11.71866 | -43.65803 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 275ea54c-257c-3864-b427-db0cfbe9f3be | -3.16793 | -50.45849 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6cae5551-df55-3352-85d7-dbf7d10f53ee | -8.6024 | -45.64612 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9abea1d7-8df7-3a9a-b588-249d227a0962 | -4.45109 | -47.92665 | 2026-10-08 04:02:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1777f3e4-62f5-33d0-9568-517abc468680 | -5.50782 | -42.82312 | 2026-10-08 04:02:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e60928e-1fe1-3ba1-be31-1da973b9b7e6 | -9.12181 | -48.51932 | 2026-10-08 04:02:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe2dc493-bd81-3a11-b9b8-d23a41eee3a8 | -6.6149 | -37.90384 | 2026-10-08 04:02:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d730952b-63ab-3c94-a7c7-45b00dffe8d8 | -7.22343 | -44.27654 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 843eb344-8770-32a7-acd8-6621f65d99a9 | -7.47053 | -42.8548 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 06612a08-638a-32c9-b90e-41934e79bb90 | -6.14514 | -47.92531 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 5622e6b1-93d4-3c09-9ef7-14b20186fe89 | -5.75157 | -42.06301 | 2026-10-08 04:02:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a41ce1bd-6cf7-3360-94e3-f0959ed38db1 | -8.78031 | -41.14943 | 2026-10-08 04:02:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e7630384-16ae-37e8-b1fa-d73cc2c5d6c7 | -7.34891 | -43.19053 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d85161a-11c7-3013-9327-173abfefdb13 | -9.47253 | -47.75521 | 2026-10-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15f8dc9c-d502-3d10-82ea-f0121092e7dc | -11.63423 | -43.69707 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 5ae44525-6f0a-318d-a368-bad47eb0f637 | -9.94349 | -43.5647 | 2026-10-08 04:02:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddabf7b4-706c-38b1-8056-66e3c213c9ea | -6.58465 | -41.5847 | 2026-10-08 04:02:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e7fb2304-3f8a-3f58-a5a1-ec16d859a8d5 | -5.75231 | -42.05859 | 2026-10-08 04:02:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e7c1b84a-d4a5-3374-8d8c-4fb2a5d5ed09 | -10.96736 | -45.39934 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7aeb9c8-e087-3152-95a6-1e4f9b4aa7a0 | -7.88078 | -44.24335 | 2026-10-08 04:02:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 816538e5-68e2-39fd-8c5e-45c18fe482bf | -7.88204 | -44.23609 | 2026-10-08 04:02:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3be47217-66a8-34d9-aea6-a69fc836deac | -8.36861 | -44.76053 | 2026-10-08 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15183688-cb65-3005-b0a2-079eb4def78a | -11.61264 | -43.66496 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47b22fac-c542-329c-91e3-c0687afd0dcf | -11.24098 | -46.24543 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| d80cd298-4853-305a-aae2-58453818bc22 | -3.18613 | -50.57061 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0abcddc-3204-3554-b537-4ba18dd7b88d | -8.28488 | -50.26604 | 2026-10-08 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5dd5d7d4-8443-3c80-beb2-1126fb3ca89c | -3.17741 | -50.5634 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6746725-921e-3a61-927c-e882ca4cd99f | -8.72478 | -45.15869 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3e3b3c8a-db1f-3e00-b1bc-b5f7cc1aee4e | -3.35679 | -50.48007 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3990aa2-af1c-3ebc-86be-3f4925c9fa83 | -6.3758 | -42.90142 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c1be5eb6-8095-30d1-aad0-954f63446892 | -5.72607 | -41.76469 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bf513ddd-4d53-302a-be86-d4a4bfe99038 | -3.20166 | -50.56092 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5060adbd-454e-36b0-a19b-5799e14a11e5 | -5.96633 | -40.91519 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 18b0d12d-88a3-3666-8d46-0efc4e972e64 | -8.22082 | -46.33661 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f795120b-8dfe-3158-8c6e-e866a98d2215 | -8.38313 | -46.2889 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21646175-d5b3-3338-9eea-be87c2efd7c2 | -10.42778 | -47.26741 | 2026-10-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 25493cae-8844-392e-8f23-85ba3dd00910 | -5.71511 | -41.76289 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| da83886c-54fc-3526-9d02-6ec382fbf616 | -10.2526 | -44.6407 | 2026-10-08 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36cda34f-be5d-3154-a9f9-3eb669f09b39 | -9.94784 | -43.49998 | 2026-10-08 04:02:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62205fff-2520-3028-99e1-73fb701ccca0 | -11.64707 | -43.69224 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 23caa02c-3050-37ad-944f-dae64c98d311 | -11.22471 | -45.24668 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c8ae647-574f-3088-8b11-18060dde7ad7 | -6.95677 | -45.26633 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcdce27d-c1ef-3e46-96a6-39ed1b476449 | -4.35383 | -43.79606 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| df2ce8b4-2dca-39ac-a9ac-4ea279a1c1c6 | -4.45174 | -47.9229 | 2026-10-08 04:02:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| c551ef62-4f20-350c-bfb8-d926e6e5dac4 | -5.50449 | -42.84291 | 2026-10-08 04:02:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 01dd2471-eb34-3ebe-ac89-4a2a4592b607 | -8.28398 | -50.27071 | 2026-10-08 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f642a0be-98fc-3eaf-af3b-2e56705fbea0 | -3.18513 | -50.55862 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d31cdf2-d566-3b58-a3c3-bf77e7f5a61d | -11.30605 | -44.83162 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c77c78b1-4aa4-3624-9ed6-d357e47afe3d | -8.60098 | -45.63821 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee6e46b0-dc92-3d7e-b3db-75b168e560e4 | -3.94632 | -49.01365 | 2026-10-08 04:02:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c6e5441-4c85-30f0-a887-6abc0e1ef5d8 | -8.06118 | -44.80707 | 2026-10-08 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7ac7bbd-ecbb-3987-b42d-6a2086927911 | -5.98543 | -40.93009 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9c9c9b26-43fd-36ed-b5b8-0bbaf9e7b7e9 | -8.72835 | -45.16364 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 750caa43-ba27-31f7-b705-e8e5f4e45293 | -3.23588 | -50.18236 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03ae60d2-b9b3-33ea-9ca1-1b1ccbe6c4e2 | -7.21306 | -44.28691 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1f11ee07-ddb2-3bcd-bfcc-62b955f08698 | -7.19928 | -45.35736 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README64.md)
