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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6ca0f13-8e01-3857-b09a-9d9053acf6a0 | -8.0721 | -42.94787 | 2025-09-30 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5712c309-a8fc-3059-b77f-02fd74c75007 | -6.09158 | -42.66144 | 2025-09-30 03:25:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 452fa9d7-4497-3e67-9352-a70205c1c7b2 | -7.9083 | -44.62498 | 2025-09-30 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9835ba75-e84d-3cbd-9e0e-b8ea769a55d7 | -5.91063 | -43.70511 | 2025-09-30 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b27fb06-cc89-39af-9763-51adc2a7be16 | -6.56478 | -43.42193 | 2025-09-30 03:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c366f9ab-673b-359f-b233-cb2f9c026fae | -6.28716 | -43.92731 | 2025-09-30 03:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 08518d23-ff45-3b03-947a-00c60097825c | -5.23115 | -43.7059 | 2025-09-30 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 15ae50ff-2aab-3ef5-99c2-ad0acaadc7a0 | -6.42823 | -43.08417 | 2025-09-30 03:25:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 51e86ee8-295d-3fd3-b528-64fb35a77fd5 | -4.89809 | -43.46995 | 2025-09-30 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| d11bf582-acec-384d-9f9e-b9ef1334fd65 | -5.42131 | -42.28946 | 2025-09-30 03:25:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b8719e8e-b4f4-314d-883f-5d73260b50ab | -5.25028 | -43.74347 | 2025-09-30 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d1c3e81-c1f8-3914-b48c-1dd092d5dc04 | -6.49792 | -44.26733 | 2025-09-30 03:25:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cc7d2d9a-2e2c-3037-81cb-baffa7fa16fd | -5.90947 | -43.7115 | 2025-09-30 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f960f53-79b2-38af-b5ba-f72fad135dfc | -7.18388 | -41.69846 | 2025-09-30 03:25:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 147c534a-477e-3e1f-bb72-8bea6600e37a | -4.8917 | -43.47704 | 2025-09-30 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ebe8dfac-68fd-3226-a843-835c472b05c7 | -5.75089 | -42.67412 | 2025-09-30 03:25:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4da18cfc-d307-347b-b597-2c1fb62e0eb7 | -7.17703 | -41.70176 | 2025-09-30 03:25:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d7dc4b38-ed56-3478-819f-db6d2866ca45 | -7.91765 | -44.61473 | 2025-09-30 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d5dc858-1435-3eeb-99b4-2d37400f9ac0 | -4.81903 | -42.76614 | 2025-09-30 03:25:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30513e28-a3d9-3178-aecf-2bcc43954d6e | -7.91075 | -44.61245 | 2025-09-30 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| acb95375-f659-3928-bfc0-887f2e667f7d | -4.89688 | -43.47653 | 2025-09-30 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 7179b25a-42d3-331e-940c-8df55d103309 | -5.03494 | -43.61875 | 2025-09-30 03:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| da49b68f-ed52-346c-8ec3-ed277423ce6c | -5.79179 | -35.6022 | 2025-09-30 03:25:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 379651c5-5485-3037-a35e-b975a28d7f70 | -6.45579 | -44.00647 | 2025-09-30 03:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3909cefc-8081-35a6-bda9-d978fb5964aa | -7.70059 | -41.28426 | 2025-09-30 03:25:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 072948f6-58a1-34af-8e6d-498edbdfd9d3 | -5.33124 | -43.73707 | 2025-09-30 03:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 80b4939d-8c9f-3593-8e8c-b7541a1fe048 | -4.81539 | -42.76194 | 2025-09-30 03:25:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bd1ca350-e809-3169-aeea-c643eee413a5 | -6.09199 | -42.66657 | 2025-09-30 03:25:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 791fed4f-ad29-3168-bbac-955bc82f457e | -5.90912 | -43.70409 | 2025-09-30 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94207ad3-1bdb-3238-952d-c57b240044dc | -5.74542 | -42.66695 | 2025-09-30 03:25:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 09082fc7-452a-36be-a4d0-25fa0bf8085f | -7.91533 | -44.62658 | 2025-09-30 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3673ffe8-753f-3775-8070-36ccc7d5efaa | -2.86218 | -40.47326 | 2025-09-30 03:25:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 42d1af37-894e-36b1-bf6e-bea6639777d4 | -4.46717 | -38.61119 | 2025-09-30 03:25:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 19a663b2-37f4-305c-9f9f-efb65cfb12c1 | -4.81232 | -42.76508 | 2025-09-30 03:25:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7b369348-b9c1-3736-845f-cdb7ff203771 | -5.42011 | -42.29308 | 2025-09-30 03:25:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 70db71af-d166-3dcb-a44a-f9622f88d2a8 | -5.52491 | -43.87667 | 2025-09-30 03:25:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c02aa8e3-6545-3985-8bee-a8a0918711a9 | -6.28842 | -43.92049 | 2025-09-30 03:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cc225f4-ff4c-3f76-9739-82d050e6e00c | -6.0991 | -42.65722 | 2025-09-30 03:25:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3014c651-098c-36c5-9243-db1e2dbe6b28 | -5.0269 | -42.99687 | 2025-09-30 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4d6da3ff-d4ba-3779-b412-52e2cfa8f96d | -4.89113 | -43.46875 | 2025-09-30 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae887031-a17d-3d3e-b6cf-d36b6f810e49 | -6.55823 | -43.41956 | 2025-09-30 03:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 47dc6377-47ae-3b58-afc9-a5a1c063a7c7 | -6.40909 | -43.76293 | 2025-09-30 03:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3d1cdbe-2a3f-3a34-89b3-cb7d01ca4d30 | -6.42928 | -43.07843 | 2025-09-30 03:25:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 75305a8b-a7e9-346c-b9df-59b6dc804d82 | -4.89866 | -43.47823 | 2025-09-30 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 6bf4ec01-9cbe-31c7-94d8-737e8a13261d | -2.86392 | -40.4729 | 2025-09-30 03:25:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 63173830-fe87-3806-8013-9a911638d5c7 | -7.90947 | -44.61898 | 2025-09-30 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ca775732-c4a3-311e-bf78-521579c7106c | -6.49674 | -44.27357 | 2025-09-30 03:25:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 972daa54-8c08-3a8e-abf2-57d6f33f631a | -6.30206 | -43.80754 | 2025-09-30 03:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 451f82cf-eae3-38db-8e5c-73dabc87f4e0 | -5.028 | -42.9908 | 2025-09-30 03:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18d26f4e-9d41-393d-8268-ccf7411a4ecf | -7.12282 | -35.10929 | 2025-09-30 03:25:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d924f448-62f3-3cba-955a-edabd8c5e0d5 | -6.70234 | -44.55426 | 2025-09-30 03:25:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c79db7f-a57c-3852-92e7-38c51409b960 | -5.72746 | -43.96682 | 2025-09-30 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9c0ffffd-1c6f-32c8-b04b-9d771b91e015 | -6.09056 | -42.66685 | 2025-09-30 03:25:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a3b6450d-75a2-3c1d-88cf-b385fa5419ef | -6.83616 | -44.8397 | 2025-09-30 03:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3d5cdd6-edfe-3e13-be99-d0dd051169b1 | -6.70071 | -44.56268 | 2025-09-30 03:25:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3093482c-ccfe-3cd1-be41-fa368d749715 | -3.88946 | -42.51811 | 2025-09-30 03:25:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b32d691b-e636-3b2c-8345-f29a34ca71aa | -7.90708 | -44.63118 | 2025-09-30 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4b45e1b5-d71a-305d-8ec4-1d56e4482cdf | -5.90676 | -43.71661 | 2025-09-30 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef6d5ceb-4530-3af7-81c6-d2e3d4a537b9 | -5.23239 | -43.69909 | 2025-09-30 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4a61a7c1-9238-3430-a657-d380455d3715 | -6.837 | -44.83249 | 2025-09-30 03:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1e4b84d-811a-3668-9fea-45d4f291ec81 | -5.51657 | -43.88241 | 2025-09-30 03:25:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| b48c7bbb-e7b8-31f5-b42d-22d0f01efa22 | -4.90103 | -43.46489 | 2025-09-30 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2b9a6d5a-f925-3907-895e-251ea3021ae0 | -3.6816 | -38.93359 | 2025-09-30 03:25:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9d633ff9-ce7d-348a-891a-2648355b1d19 | -5.76508 | -43.84091 | 2025-09-30 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be1400fc-ca1f-3b86-a179-f30dcc7a783e | -3.88278 | -42.51694 | 2025-09-30 03:25:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 811f2ee8-8e75-378b-b4fb-7c7f5fa63e2d | -6.0981 | -42.66253 | 2025-09-30 03:25:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bb8c6b38-111a-35fb-8ba0-13d509b2167c | -4.78877 | -40.54794 | 2025-09-30 03:25:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 33d18321-5503-3b7f-b4f5-6afd6f815580 | -6.29207 | -43.92654 | 2025-09-30 03:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c1f6ed55-79aa-34af-af87-4e5d73f6465d | -4.81434 | -42.76771 | 2025-09-30 03:25:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c952b48d-6013-3855-b784-b3f14aa40225 | -5.75185 | -42.66879 | 2025-09-30 03:25:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 212f8f8c-cb27-3193-8e9f-fce66956d159 | -6.46269 | -44.00829 | 2025-09-30 03:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c86031a4-73dc-3073-bd54-4a0185d6b162 | -4.39833 | -44.08369 | 2025-09-30 03:25:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a2e43ccf-68fa-3253-a73e-54f573d6a351 | -5.42105 | -42.28777 | 2025-09-30 03:25:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b56ad65e-fe13-3002-afe2-7fb9e7917927 | -4.86878 | -37.45375 | 2025-09-30 03:25:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 45891732-8755-39b2-b5d7-754530b3dc07 | -7.91192 | -44.60648 | 2025-09-30 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71fabcbc-4a0b-30b7-81ed-49140449a838 | -7.91415 | -44.63266 | 2025-09-30 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 95ac7298-79b7-3bfe-b503-19b2bd260b93 | -6.2953 | -43.92233 | 2025-09-30 03:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7199a331-e93d-3b26-9431-e737b577e7dc | -5.24906 | -43.74998 | 2025-09-30 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 62e85d52-41a9-3fcd-b866-59ea265d3ad1 | -5.5178 | -43.8757 | 2025-09-30 03:25:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9faa58c8-f6fa-3f42-97a6-f239414b8680 | -4.39956 | -44.07662 | 2025-09-30 03:25:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8c63d179-b0ef-37d2-b4d7-f9e0ee094529 | -6.76604 | -37.89533 | 2025-09-30 03:25:00 | NPP-375D | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d4b0760b-91e7-3dbf-a8c4-88da1169bd23 | -6.09709 | -42.66794 | 2025-09-30 03:25:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c663e0f9-de4d-36b5-9174-899070e8dcf8 | -6.09948 | -42.6623 | 2025-09-30 03:25:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 45532b48-2d9a-3f47-a489-831b02bf082f | -4.79305 | -40.54872 | 2025-09-30 03:25:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f8e9283d-5c3d-3ed5-a0af-d39674edd607 | -6.74315 | -34.98564 | 2025-09-30 03:25:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6984f9ab-e6be-3862-b94a-cab7df8cf4d7 | -3.88674 | -42.5139 | 2025-09-30 03:25:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab5ddc65-0e81-32a0-b3e6-09b94c7401c0 | -4.39812 | -44.08791 | 2025-09-30 03:25:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 41a43968-044a-3024-b127-c1aec74aa6c5 | -6.83551 | -44.84033 | 2025-09-30 03:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58b93dff-b306-3fdd-a49f-fa29be9b9173 | -5.40869 | -37.7025 | 2025-09-30 03:25:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5c46d1cd-d0e0-321b-ac7e-f2a6e5fbc59e | -5.82836 | -42.79753 | 2025-09-30 03:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| deb4516e-8dc4-3bcc-86d1-2b8e3d8d8964 | -14.16906 | -44.30501 | 2025-09-30 03:28:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92808d74-bcd8-33f9-aa7f-c1abd191de1b | -15.7755 | -43.67239 | 2025-09-30 03:28:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24490038-435a-3a8a-a4bd-f5f165f57bd7 | -11.45949 | -45.01687 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f6fa9f4-33b2-3d4d-a429-8b795630141b | -15.06961 | -45.05832 | 2025-09-30 03:28:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51758612-0479-31f5-bb55-306ba3fb4190 | -13.0115 | -44.11608 | 2025-09-30 03:28:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c4affdc0-0bba-32f5-8f2a-efcf8ad77bad | -11.67558 | -44.30106 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da83bb9e-8878-3ffc-8c71-8c79fa2e36c8 | -14.64112 | -46.96924 | 2025-09-30 03:28:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 64c1b8a7-e0b9-3f26-abea-bb73b024ee18 | -11.75867 | -44.74017 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84b3353e-7c6c-3b2b-ae99-b16465627e8a | -11.44711 | -43.51033 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 031c64c6-61cc-3e50-ab29-88da7c1d4b0a | -10.19713 | -44.89059 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README17.md)
